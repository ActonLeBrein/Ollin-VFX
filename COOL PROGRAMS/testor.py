d = {5:[4,2],9:[3,5],3:[7,6]}
d[4] = [10,14]
print d
print d.keys()
print d.values()
k = d.keys()
v = d.values()
r = []
for i in k:
	for j in v:
		print i,j
		if i in j:	
			r.append(i)
			for a, b in d.iteritems():
				if b == j:
					print a,j,i
print r
for l in r:
	k.remove(l)
	del d[l]
print k,d