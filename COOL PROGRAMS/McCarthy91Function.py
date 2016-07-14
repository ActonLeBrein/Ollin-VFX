def m91(n):
    if n > 100:
    	print 'finished %s' % (n - 10)
        return n - 10
    else:
    	n = n + 11
    	print 'halfway there %s' % n
        return m91(m91(n))

#m91(15)

def G(n):
	if n <= 0:
		print 'G fisnish at last!!!! %s' % n
		return 0
	else:
		print 'G Still on the run %s' % n
		return n - G(G(n - 1))

#G(10)

def H(n):
	if n <= 0:
		print 'H fisnish at last!!!! %s' % n
		return 0
	else:
		print 'H Still on the run %s' % n
		return n - H(H(H(n - 1)))

#H(10)

def M(n):
	if n <= 0:
		print 'M fisnish at last!!!! 0'
		return 0
	else:
		print 'M Still on the run %s' % n
		return n - F(M(n - 1))

def F(n):
	if n <= 0:
		print 'F fisnish at last!!!! 1'
		return 1
	else:
		print 'F Still on the run %s' % n
		return n - M(F(n - 1))

#F(5)
#M(5)

def Q(n):
	if n <= 2:
		print 'Q finish at last %s' % n
		return 1
	else:
		print 'Q Still on the run %s' % n
		return Q(n - Q(n - 1)) + Q(n - Q(n - 2))

#Q(8)