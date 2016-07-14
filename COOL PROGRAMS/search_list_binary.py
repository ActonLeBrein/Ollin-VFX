class Binary_Search(object):

	def __init__(self, lis, x):
		self.lis = lis
		self.lis.sort()
		self.x = x
		self.pos = abs((len(lis)-1) / 2)
		print self.lis

	def position(self):
		return self.lis[self.pos]

	def in_between(self):
		if (self.pos > -1) and (self.pos < (len(self.lis) -1)):
			if self.lis[self.pos-1] > self.x > self.lis[self.pos+1]:
				return True
			else:
				return False
		else:
			return False

	def mov_left(self):
		self.pos -= 1

	def mov_right(self):
		self.pos += 1

	def check_val(self):
		if self.position() == self.x:
			return True
		else:
			return False

	def check_pos(self):
		if (self.position() > self.x):
			if (self.pos > -1):
				self.mov_left()
				return True
			else:
				return False
		else:
			if (self.pos < (len(self.lis) -1)):
				self.mov_right()
				return True
			else:
				return False

def B_S(lis,elem):
	bs = Binary_Search(lis,elem)
	st = bs.check_val()
	elem_in = False
	if st:
		print "Element in list at first attempt"
	else:
		while (st != True):
			if bs.check_val() == True:
				st = bs.check_val()
				elem_in = bs.check_val()
			elif bs.check_pos() == False:
				st = True
			else:
				bs.check_pos()
		if elem_in:
			print "Element in list DONE"
		else:
			print "Element not in list NO"

a = Binary_Search(lis = [4,23,76,89,1,0,7], x = 76)
print a.position()
print a.check_val()
print a.check_pos()
print a.position()
print a.check_val()
print a.check_pos()
print a.position()
print a.check_val()
print a.check_pos()
print a.position()
print a.check_val()
print a.check_pos()
B_S([4,23,76,89,1,-1,0,7],0)