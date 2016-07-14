import random

def Axiom():
	return 'MI'

def check_for_U(s):
	l = list(s)
	if l[len(l)-1] == 'U':
		return True
	else:
		return False

def find_pattern(s):
	l = list(s)
	del l[0]
	p = ['I','U']
	for i in range(len(l)):
		if l[i*2:i*2+len(p)] == []:
			print 'There is a spoon %s in %s' % (''.join(p),s)
			return True
		elif l[i*2:i*2+len(p)] != p:
			f = False
			print 'There is no spoon %s in %s' % (''.join(p),s)
			return False

def rule1(s,t):
	l = list(s)
	if l[len(l)-1] == 'I':
		l.append('U')
		s = ''.join(l)
		t -= 1
		print 'R1 STEP %i: There was a change %s' % (t,s)
		return (s,t)
	else:
		print 'R1 STEP %i: No change %s' % (t,s)
		return (s,t)

def rule2(s,t):
	l = list(s)
	l = l + l[1:len(l)]
	s = ''.join(l)
	t -= 1
	print 'R2 STEP %i: Double pattern %s' % (t,s)
	return (s,t)

def rule3(s,t):
	p = ['I','I','I']
	c = []
	l = list(s)
	for i in range(len(l)):
		if l[i:i+len(p)] == p:
			c.append((i,i+len(p)))
	if len(c) > 0:
		d = c[random.randrange(len(c))]
		l[d[0]:d[1]] = 'U'
		s = ''.join(l)
		t -= 1
		print 'R3 STEP %i: Subtitute III for U %s' % (t,s)
		return (s,t)
	else:
		print 'R3 STEP %i: No subtitution in %s' % (t,s)
		return (s,t)

def rule4(s,t):
	p = ['U','U']
	c = []
	l = list(s)
	for i in range(len(l)):
		if l[i:i+len(p)] == p:
			c.append((i,i+len(p)))
	if len(c) > 0:
		d = c[random.randrange(len(c))]
		del l[d[0]:d[1]]
		s = ''.join(l)
		t -= 1
		print 'R4 STEP %i: Delettion of UU %s' % (t,s)
		return (s,t)
	else:
		print 'R4 STEP %i: No deletion in %s' % (t,s)
		return (s,t)

def MIU(s,t):
	rules = {1:rule1, 2:rule2, 3:rule3, 4:rule4}
	ran = random.randrange(1,5)
	if (t == 0) or (s == 'MU'):
		print 'Final result %s' % s
		return s
	else:
		if s == '':
			s = Axiom()
			print '%i number of steps in %s' % (t,s)
			v1 = rules[ran]
			v2 = v1(s,t)
			MIU(v2[0],v2[1])
		elif find_pattern(s):
			print 'Pattern IU is present in %s TT_TT' % s
			return s
		elif check_for_U(s):
			v1 = rules[ran]
			v2 = v1(s,t)
			MIU(v2[0],v2[1])
		else:
			v1 = rules[ran]
			v2 = v1(s,t)
			MIU(v2[0],v2[1])

MIU('',7)