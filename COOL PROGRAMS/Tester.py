b = {1:[3,2],2:[19,8],3:[70,10],10:[11,20],70:[5,88],20:[76,56],19:[787,999],88:[1002,10254],10254:[444],444:[4785,12548]}
c = {}

def tree_road(t1,t2,l,v):
	if len(v) == 0:
		v.append(l)
	else:
		pass
	try:
		t2[max(t1[l])] = [min(t1[l])]
		try:
			t2[max(t1[l])] = t2[max(t1[l])] + [max(t1[max(t1[l])])]
		except:
			pass
		print 'father %s sons %s road %s' % (l,t1[l],t2)
		tree_road(t1,t2,max(t1[l]),v)
	except:
		for m in t1.keys():
			if v[0] in t1[m]:
				t1[m].remove(v[0])
				t1[m] = t1[m] + [max(t1[v[0]])]
		del t1[v[0]]
		for k in t2.keys():
			if k in t1.keys():
				del t1[k]
			else:
				pass
		for n in t2.keys():
			if n in t2[n]:
				del t2[n]
		t3 = dict(t1.items() + t2.items())
		print 'final tree %s' % t3

def sort_tree(t):
	for i in t.keys():
		t[i].sort()
	return t

print sort_tree(b)
tree_road(sort_tree(b),c,1,[])