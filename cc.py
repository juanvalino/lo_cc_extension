#  cc.py - Pyuno bridge to implement new functions for LibreOffice Calc
#
#  Copyright (c) 2018 Juan Antonio Valino Garcia
#
#  license: GNU LGPL
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3 of the License, or (at your option) any later version.
#
#  Based on Mark Brooker LOC-Extension
#

import unohelper

from com.cc import CC
from cryptocompare import get_historical_price
from csv import DictReader, DictWriter
from datetime import datetime, timedelta
from os.path import expanduser, isfile, join
from unohelper import Base, ImplementationHelper

class CCImpl(Base, CC):
    """Define the main class for the CC extension."""

    def __init__(self, ctx):
        self.ctx = ctx

    def getCCHistoricalPrice(self, fsym, tsym, exchange, date):
        """Return historical price.

        Args:
            fsym (string): symbol from wich get the price (from symbol)
            tsym (string): symbol in which the price must be get (to symbol)
            exchange (string): exchange to get the price from (can be an empty
                string '' if you don't want to use a concrete exchange)
            date (float): date in LibreOffice calc (days since 1899/12/31)

        Returns:
            float: historical price
        """

        home = expanduser("~")
        cache_file = join(home, ".cc_cache.csv")
        fieldnames = ["timestamp", "fsym", "tsym", "price"]
        date_base_calc = datetime(1899, 12, 30)
        date_base_unix = datetime(1970, 1, 1)
        delta = timedelta(days=date)
        timestamp = (date_base_calc + delta - date_base_unix).total_seconds()

        # Read cache CSV file

        price = None
        if isfile(cache_file):
            file = open(cache_file, "r")
            reader = DictReader(file, fieldnames=fieldnames)
            for row in reader:
                if row["timestamp"] == str(timestamp) \
                   and row["fsym"] == str(fsym) \
                   and row["tsym"] == str(tsym):
                   price = row["price"]
                   break
            file.close()

        # Call cryptocompare API and save price in cache

        if price is None:
            if len(exchange) != 0:
                result = get_historical_price(fsym,
                                              tsym,
                                              timestamp=timestamp,
                                              exchange=exchange)
            else:
                result = get_historical_price(fsym,
                                              tsym,
                                              timestamp=timestamp)
            price = result[fsym][tsym]
            row = { "timestamp": timestamp,
                    "fsym": fsym,
                    "tsym": tsym,
                    "price": price }
            file = open(cache_file, "a")
            writer = DictWriter(file, fieldnames=fieldnames)
            writer.writerow(row)
            file.close()

        return float(price)

def createInstance(ctx):
    return CCImpl(ctx)

g_ImplementationHelper = ImplementationHelper()
g_ImplementationHelper.addImplementation(createInstance,
                                         'com.cc.python.CCImpl',
                                         ('com.sun.star.sheet.AddIn',),)
