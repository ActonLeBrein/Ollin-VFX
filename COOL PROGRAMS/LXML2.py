import xml.etree.ElementTree as ET
import sys
import os

def get_file_path(filename):
    currentdirpath = os.getcwd()
    file_path = os.path.join(os.getcwd(), filename)
    return file_path

path = get_file_path('namespaces.xml')
with open(path, 'rU') as xml_file:
    array = ''
    for line in xml_file:
        array = array + line
    print array
xml_text = array

path = get_file_path('countries.xml')
with open(path, 'rU') as xml_file:
    array = ''
    for line in xml_file:
        array = array + line
    print array
countriesdata = array

tree = ET.parse('countries.xml')
root = tree.getroot()
print root

for country in root.iter('country'):
	print country.attrib['name']
	print country.find('rank').text
	print country.find('year').text
	print country.find('gdppc').text
	for neighbor in country.iter('neighbor'):
		print neighbor.attrib['name'], neighbor.attrib['direction']
	print '--------------------------'

for rank in root.iter('rank'):
	new_rank = int(rank.text) + 1
	rank.text = str(new_rank)
	rank.set('updated', 'yes')

tree.write('countries.xml')

a = ET.Element('a')
b = ET.SubElement(a, 'b')
c = ET.SubElement(a, 'c')
d = ET.SubElement(c, 'd')
ET.dump(a)

print xml_text
root = ET.fromstring(xml_text)
for actor in root.findall('{http://people.example.com}actor'):
	name = actor.find('{http://people.example.com}name')
	print name.text
	for char in actor.findall('{http://characters.example.com}character'):
		print ' |-->', char.text

ns = {'real_person': 'http://people.example.com','role': 'http://characters.example.com'}

for actor in root.findall('real_person:actor', ns):
	name = actor.find('real_person:name', ns)
	print name.text
	for char in actor.findall('role:character', ns):
		print ' |-->', char.text

root = ET.fromstring(countriesdata)

print root.findall(".")[0].tag
for j in root.findall("./country/neighbor"):
	print j.attrib['name'],j.attrib['direction']
	print j.tag
print root.findall(".//year/..[@name='Singapore']")[0].attrib['name']
print root.findall(".//*[@name='Singapore']/year")[0].text
for i in root.findall(".//neighbor[2]"):
	print i.attrib['name'],i.attrib['direction']
	print i.tag

print root.findall(".//country/neighbor/..[@name][2]")[0].attrib