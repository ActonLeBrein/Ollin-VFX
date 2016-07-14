class TreeClass():
	def __init__(self):
		self.tree = {}
		self.spare_tree = {}
		self.carrier = []

	def parents(self):
		return self.tree.keys()

	def kids(self):
		return self.tree.values()

	def childs(self,elem):
		return self.tree[elem]

	def father(self,elem):
		for a, b in self.tree.iteritems():
			if elem in b:
				return a

	def number_children(self,elem):
		return len(self.tree[elem])

	def left(self,elem):
		return self.tree[elem][0]

	def right(self,elem):
		return self.tree[elem][1]

	def top_tree(self):
		k = self.tree.keys()
		v = self.tree.values()
		r = []
		if len(k) == 0:
			return -3
		else:
			for i in k:
				for j in v:
					if i in j:
						r.append(i)
			for l in r:
				k.remove(l)
			return k[0]

	def look(self,elem):
		if self.top_tree() == elem:
			print "Element %s is at the top of the tree, children are %s" % (elem, self.childs(elem))
		elif self.number_children(elem) == 0:
			print "Element %s has no childre, father is %s" % (elem,self.father(elem))
		else:
			print "Element %s father is %s, children are %s" % (elem, self.father(elem), self.childs(elem))

	def add1(self,elem):
		if self.top_tree() == -3:
			self.tree[elem] = []
			print self.tree
		else:
			pointer = self.top_tree()
			self.add2(pointer,elem)

	def add2(self,top,elem):	
		if top == elem:
			print "Element %s already in tree %s" % (elem, self.tree)
		elif top > elem:
			if self.number_children(top) == 0:
				self.tree[top] = self.childs(top) + [elem]
				self.tree[elem] = []
				print self.tree
				return self.tree
			elif self.number_children(top) == 1:
				self.tree[top] = self.childs(top) + [elem]
				self.tree[top].sort()
				self.tree[elem] = []
				print self.tree
				return self.tree
			else:
				self.add2(self.left(top),elem)
		else:
			if self.number_children(top) == 0:
				self.tree[top] = self.childs(top) + [elem]
				self.tree[elem] = []
				print self.tree
				return self.tree
			elif self.number_children(top) == 1:
				self.tree[top] = self.childs(top) + [elem]
				self.tree[top].sort()
				self.tree[elem] = []
				print self.tree
				return self.tree
			else:
				self.add2(self.right(top),elem)

	def remove(self,elem):
		if len(self.carrier) == 0:
			self.carrier.append(elem)
		else:
			pass
		try:
			self.spare_tree[max(self.tree[elem])] = [min(self.tree[elem])]
			try:
				self.spare_tree[max(self.tree[elem])] = self.spare_tree[max(self.tree[elem])] + [max(self.tree[max(self.tree[elem])])]
			except:
				pass
			self.remove(max(self.tree[elem]))
		except:
			for i in self.tree.keys():
				if self.carrier[0] in self.tree[i]:
					self.tree[i].remove(self.carrier[0])
					self.tree[i] = self.tree[i] + [max(self.tree[self.carrier[0]])]
			del self.tree[self.carrier[0]]
			for j in self.spare_tree.keys():
				if j in self.tree.keys():
					del self.tree[j]
				else:
					pass
			for k in self.spare_tree.keys():
				if k in self.spare_tree[k]:
					del self.spare_tree[k]
			t = dict(self.tree.items() + self.spare_tree.items())
			self.tree = t
			self.spare_tree = {}
			self.carrier = []
			return self.tree

	def __str__(self):
		p1 = self.top_tree()
		p2 = self.parents()
		ret = ""
		ret += "Tree %s" % self.tree
		ret += "\n"
		ret += "Top of tree %s " % p1
		ret += "Childrens are %s" % self.tree[p1]
		ret += "\n"
		p2.remove(p1)
		for i in p2:
			ret+= "Father of %s is %s -> " % (i,self.father(i))
			if len(self.tree[i]) != 0:
				ret += "Childrens are %s" % self.tree[p1]
				ret += "\n"
			else:
				ret += "Has no children"
				ret += "\n"
		return ret

if __name__ == "__main__":
	test = TreeClass()
	test.add1(18)
	test.add1(20)
	test.add1(2)
	test.add1(3)
	test.add1(130)
	test.add1(20000)
	test.add1(5421)
	test.add1(1)
	test.add1(0)
	test.add1(-11)
	test.add1(7)
	test.add1(34)
	test.add1(30)
	test.remove(20000)
	print test