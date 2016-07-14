
c = 3-5j
print ('The complex number {0} is formed from the real part {0.real} and the imaginary part {0.imag}.').format(c)
print 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')

class Point:
    def __init__(self, x, y):
    	self.x, self.y = x, y
    def __str__(self):
    	return 'Point({self.x}, {self.y})'.format(self=self)

print str(Point(4, 2))

print "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
print "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)

for align, text in zip('<^>', ['left', 'center', 'right']):
	print '{0:{fill}{align}100}'.format(text, fill=align, align=align)