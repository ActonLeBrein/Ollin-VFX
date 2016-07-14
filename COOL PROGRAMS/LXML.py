from sys import exit
from lxml import etree
import sys
import os

def get_file_path(filename):
    currentdirpath = os.getcwd()
    file_path = os.path.join(os.getcwd(), filename)
    return file_path

path = get_file_path('error.xml')
with open(path, 'rU') as xml_file:
    array = ''
    for line in xml_file:
        array = array + line
    print array
response = array

try:
    doc = etree.XML(response.strip())
    code = doc.findtext('code')
    print code
except etree.XMLSyntaxError:
    print 'XML parsing error. OOOOHHH NOSEEEEEEEE!!!!'
    exit(1)

if code == '200':
    # store the id somewhere
    id = doc.findtext('id')
    print id
else:
    # handle errors, do more stuff
    errors = doc.findtext('errors')
    print errors
    exit(1)

exit(0)