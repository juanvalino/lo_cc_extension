#!/bin/bash
#
#  compile.sh - Compile LibreOffice addon
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
#  To use this script you need the following software:
#
#    - cryptocompare python library
#    - libreoffice-sdk
#    - libreoffice-ure
#    - ucpp
#    - zip

# Setup paths

export LIBREOFFICEPATH=/usr/lib64/libreoffice
export LIBREOFFICEPROGRAM=$LIBREOFFICEPATH/program
export LIBREOFFICESDK=$LIBREOFFICEPATH/sdk
export PATH=$PATH:$LIBREOFFICEPROGRAM:$LIBREOFFICESDK/bin

# Load SDK environment

$LIBREOFFICESDK/setsdkenv_unix.sh

# Setup directories

mkdir -p $PWD/CC/META-INF

# Compile the binaries

idlc -I $LIBREOFFICESDK/idl $PWD/CC.idl
regmerge -v $PWD/CC/CC.rdb UCR $PWD/CC.urd
rm $PWD/CC.urd

# Copy extension files and generate metadata

cp -f $PWD/cc.py $PWD/CC
python $PWD/metainfo.py

# Package into oxt file

rm -f $PWD/CC.oxt
pushd $PWD/CC/
zip -r $PWD/CC.zip ./*
popd
mv $PWD/CC/CC.zip $PWD/CC.oxt
rm -Rf CC
