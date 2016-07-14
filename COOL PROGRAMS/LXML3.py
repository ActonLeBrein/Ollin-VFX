import xml.etree.ElementTree as ET
import sys
import os

def get_file_path(filename):
    currentdirpath = os.getcwd()
    file_path = os.path.join(os.getcwd(), filename)
    return file_path

path = get_file_path('expected.xml')
with open(path, 'rU') as xml_file:
    array = ''
    for line in xml_file:
        array = array + line
    print array
xml_text = array

root = ET.fromstring(xml_text)

print root.findall(".")[0].attrib
for j in root.findall("./dir"):
	print j.tag,j.attrib
print root.findall("./*[@name='common']")[0].attrib['name']
for i in root.findall("./*[@name='common']/dir"):
	print i.tag,i.attrib['name']
print root.findall("./dir/*[@name='scans']")[0].attrib['name']
for k in root.findall("./dir/*[@name='scans']/dir"):
	print k.tag,k.attrib['name']

path = get_file_path('command.xml')
with open(path, 'rU') as xml_file:
    array = ''
    for line in xml_file:
        array = array + line
    print array
xml_text = array

root = ET.fromstring(xml_text)

for l in root.findall("."):
	print 'password |--> ' + l.attrib['password']
	print 'command |--> ' + l.attrib['command']
	print 'user |--> ' + l.attrib['user']
for n in root.findall("./"):
	print 'clientVersion |--> ' + n.attrib['clientVersion']
	print 'clientType |--> ' + n.attrib['clientType']