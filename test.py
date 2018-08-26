#  test.py - Test CC functions through the python console
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
# Based on Mark Brooker LOC-Extension
#

from __future__ import print_function

import sys
import os
import inspect
import getopt

sys.path.append("/usr/lib64/libreoffice/program")

# Add current directory to path to import module
cmd_folder = os.path.realpath(os.path.abspath
                              (os.path.split(inspect.getfile
                                             ( inspect.currentframe() ))[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

import cc

def main(argv):
    main_cc = cc.CCImpl(argv)
    arg_fsym = ''
    arg_tsym = ''
    arg_exchange = ''
    arg_date = ''

    opts, args = getopt.getopt(argv, 'f:t:e:d:',
                                     ['from=','to=','exchange=','date='])

    for opt, arg in opts:
        if opt in ('-f', '--from'):
            arg_fsym = arg
        elif opt in ('-t', '--to'):
            arg_tsym = arg
        elif opt in ('-e', '--exchange'):
            arg_exchange = arg
        elif opt in ('-d', '--date'):
            arg_date = arg

    print("fsym: " + arg_fsym)
    print("tsym: " + arg_tsym)
    print("exchange: " + arg_exchange)
    print("date: " + arg_date)
    cc_test(main_cc,
            arg_fsym,
            arg_tsym,
            arg_exchange,
            float(arg_date))

def cc_test(cc, fsym, tsym, exchange, date):
    result = cc.getCCHistoricalPrice(fsym, tsym, exchange, date)
    print("price: " + str(result))
    sys.exit()

if __name__ == '__main__':
    main(sys.argv[1:])
