#  metainfo.py - Generate XML for CC Extension
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

from os import getcwd

# Setup extension variables

extension_id = 'com.cc'
extension_version = '1.0.0'
extension_displayname = 'CryptoCompare Extension: LibreOffice Calc market functions.'
extension_publisher_link = 'https://github.com/juanvalino/lo_cc_extension'
extension_publisher_name = 'Juan Antonio Valino Garcia'

# Get current dir

current_dir = getcwd()

# Generate description.xml

description_xml = open(current_dir + '/CC/description.xml', 'w')

description_xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
description_xml.write('<description\n')
description_xml.write('xmlns="http://openoffice.org/extensions/description/2006"\n')
description_xml.write('xmlns:d="http://openoffice.org/extensions/description/2006"\n')
description_xml.write('xmlns:xlink="http://www.w3.org/1999/xlink">\n')
description_xml.write('  <dependencies>\n')
description_xml.write('    <OpenOffice.org-minimal-version value="2.4" d:name="OpenOffice.org 2.4"/>\n')
description_xml.write('  </dependencies>\n')
description_xml.write('  <identifier value="' + extension_id + '"/>\n')
description_xml.write('  <version value="' + extension_version + '"/>\n')
description_xml.write('  <display-name>\n')
description_xml.write('    <name lang="en">' + extension_displayname + '</name>\n')
description_xml.write('  </display-name>\n')
description_xml.write('  <publisher>\n')
description_xml.write('    <name xlink:href="' + extension_publisher_link + '" lang="en">' + extension_publisher_name + '</name>\n')
description_xml.write('  </publisher>\n')
description_xml.write('  <extension-description>\n')
description_xml.write('    <src xlink:href="description-en-US.txt" lang="en"/>\n')
description_xml.write('  </extension-description>\n')
description_xml.write('</description>\n')

description_xml.close

# Generate manifest.xml

def add_manifest_entry(xml_file, file_type, file_name):
    xml_file.write('<manifest:file-entry manifest:media-type="application/vnd.sun.star.' + file_type + '"\n')
    xml_file.write('    manifest:full-path="' + file_name + '"/>\n')

manifest_xml = open(current_dir + '/CC/META-INF/manifest.xml', 'w')

manifest_xml.write('<manifest:manifest>\n');
add_manifest_entry(manifest_xml, 'uno-typelibrary;type=RDB', 'CC.rdb')
add_manifest_entry(manifest_xml, 'configuration-data', 'CC.xcu')
add_manifest_entry(manifest_xml, 'uno-component;type=Python', 'cc.py')
manifest_xml.write('</manifest:manifest>\n')

manifest_xml.close

# Generate cc.xcu (configuration file for the extension)

instance_id = 'com.cc.python.CCImpl'
excel_addin_name = ''

def define_function(xml_file, function_name, description, parameters):
    xml_file.write('      <node oor:name="' + function_name + '" oor:op="replace">\n')
    xml_file.write('        <prop oor:name="DisplayName">\n')
    xml_file.write('          <value xml:lang="en">' + function_name + '</value>\n')
    xml_file.write('        </prop>\n')
    xml_file.write('        <prop oor:name="Description">\n')
    xml_file.write('          <value xml:lang="en">' + description + '</value>\n')
    xml_file.write('        </prop>\n')
    xml_file.write('        <prop oor:name="Category">\n')
    xml_file.write('          <value>Add-In</value>\n')
    xml_file.write('        </prop>\n')
    xml_file.write('        <prop oor:name="CompatibilityName">\n')
    xml_file.write('          <value xml:lang="en">AutoAddIn.CC.' + function_name + '</value>\n')
    xml_file.write('        </prop>\n')
    xml_file.write('        <node oor:name="Parameters">\n')

    for p, desc in parameters:
        p_name = p.strip('[]')
        xml_file.write('          <node oor:name="' + p_name + '" oor:op="replace">\n')
        xml_file.write('            <prop oor:name="DisplayName">\n')
        xml_file.write('              <value xml:lang="en">' + p_name + '</value>\n')
        xml_file.write('            </prop>\n')
        xml_file.write('            <prop oor:name="Description">\n')
        xml_file.write('              <value xml:lang="en">' + desc + '</value>\n')
        xml_file.write('            </prop>\n')
        xml_file.write('          </node>\n')

    xml_file.write('        </node>\n')
    xml_file.write('      </node>\n')

xcu_xml = open(current_dir + '/CC/CC.xcu', 'w')

xcu_xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
xcu_xml.write('<oor:component-data xmlns:oor="http://openoffice.org/2001/registry" xmlns:xs="http://www.w3.org/2001/XMLSchema" oor:name="CalcAddIns" oor:package="org.openoffice.Office">\n')
xcu_xml.write('<node oor:name="AddInInfo">\n')
xcu_xml.write('  <node oor:name="' + instance_id + '" oor:op="replace">\n')
xcu_xml.write('    <node oor:name="AddInFunctions">\n')

define_function(xcu_xml, \
    'getCCHistoricalPrice', 'Fetches CryptoCompate historical price.', \
    [('fsym', 'Source symbol'), ('tsym', 'Target symbol'), ('exchange', 'Exchange'), ('date', 'Date')])

xcu_xml.write('    </node>\n')
xcu_xml.write('  </node>\n')
xcu_xml.write('</node>\n')
xcu_xml.write('</oor:component-data>\n')

xcu_xml.close
