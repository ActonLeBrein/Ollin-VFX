import inspect
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.dom import minidom
from xml.etree import ElementTree

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

class Market(object):

    def __init__(self,):
        self.grocery = self.GROCERY
        self.electronics = self.ELECTRONICS

    def GROCERY(self,):

        self.item1 = "banana"
        self.item2 = "tomato"
        self.item3 = "apple"

    def ELECTRONICS(self,):

        self.item1 = "laptop"
        self.item2 = "camera"
        self.item3 = "mobile"

def obj_to_xml(obj):
    elem = Element(obj.__class__.__name__)
    for name, method in inspect.getmembers(obj, inspect.ismethod):
        if name in obj.__dict__.keys():
            child = Element(name)
            method()
            for gname in method.__code__.co_names: 
                gchild = Element(gname)
                gchild.text = str(obj.__dict__[gname])
                child.append(gchild)

            elem.append(child)

    return elem

market = Market()
print 'LAME OUTPUT'
print '<?xml version="1.0" encoding="utf-8"?>%s' % tostring(obj_to_xml(market))

top = Element('top')

comment = Comment('Generated for PyMOTW')
top.append(comment)

child = SubElement(top, 'child', {'ans':'123'})
child.text = 'This child contains text.'

child_with_tail = SubElement(top, 'child_with_tail')
child_with_tail.text = 'This child has regular text.'
child_with_tail.tail = 'And "tail" text.'

child_with_entity_ref = SubElement(top, 'child_with_entity_ref')
child_with_entity_ref.text = 'This & that'

print 'AWESOME OUTPUT'
print prettify(top)