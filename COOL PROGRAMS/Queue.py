class Queue():
	def __init__(self):
		self.q = []

	def add(self, elem):
		self.q.insert(0,elem)

	def remove(self):
		self.q.pop()

	def show(self):
		print self.q

test = Queue()
test.add(5)
test.add(3)
test.add(8)
test.add(1)
test.show()
test.remove()
test.show()

class Stack():
	def __init__(self):
		self.s = []

	def add(self, elem):
		self.s.append(elem)

	def remove(self):
		self.s.pop(0)

	def show(self):
		print self.s

test = Stack()
test.add(2)
test.add(5)
test.add(1)
test.add(3)
test.show()
test.remove()
test.show()
