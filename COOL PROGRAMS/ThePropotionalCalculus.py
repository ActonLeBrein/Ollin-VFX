#!/usr/bin/python
 # -*- coding: utf-8 -*-

import random
import re

# ~ = NOT
# & = AND
# | = OR
# % = THEN

symbols = ["'","~","P","Q","R","&","|","%","{","<","}",">"]
symbol_values = {"'":163,"~":223,"P":444,"Q":999,"R":888,"&":161,"|":616,"%":633,"{":212,"}":213,"<":312,">":313}
atoms_values = {}

def atoms():
	a = symbols[random.randrange(2,5)]
	states(a)
	print a
	return a

def tilde(s):
	if random.randrange(0,2) == 1:
		l = [symbols[1]]
		l.append(s)
		wfs = ''.join(l)
		print 'tilde applied %s' % wfs
		return tilde(wfs)
	else:
		print 'nothing %s' % s
		return s

def prime(s):
	if random.randrange(0,2) == 1:
		l = list(s)
		l.append(symbols[0])
		wfs = ''.join(l)
		print 'prime applied %s' % wfs
		return prime(wfs)
	else:
		print 'nothing %s' % s
		return s

def states(a):
	if random.randrange(0,2) == 1:
		atoms_values[a] = True
	else:
		atoms_values[a] = False

def markers_connectors(x,y):
	ran = random.randrange(8,10)
	l = [symbols[ran]]
	l.append(x)
	l.append(symbols[random.randrange(5,8)])
	l.append(y)
	l.append(symbols[ran+2])
	wfs = ''.join(l)
	print wfs
	return wfs

def calculate(s):
	l = list(s)
	r = []
	for i in l:
		r.append(symbol_values[i])
	addition = sum(r)
	union = map(str,r)
	union = ''.join(union)
	union = int(union)
	print addition
	print union

def check_regex(s):
	match = re.search(r"([<{]~*[PQR]'*[&|%])+~*[PQR]'*[}>]+",s)
	if match:
		print 'match found %s' % match.group()
		return True
	else:
		print 'no match found'
		return False

def fantasy_rule(s):
	match = re.search(r"(<~*[PQR]'*[&|%])+~*[PQR]'*(>)+",s)
	if match:
		print 'there is a fantasy rule %s' % match.group()
		inner_fantasy_rule(match.group())
	else:
		print 'no fantasy rule'
		return False

def inner_fantasy_rule(s):
	match = re.search(r"(<~*[PQR]'*[&|%]~*[PQR]'*>)+",s)
	if match:
		print 'there is an inner fantasy rule %s' % match.group()
		invert_symbols(match.group())
	else:
		print 'no inner fantasy rule'
		return False

def add_tilde(l,p):
	atoms_values[l[p]] = not l[p]
	l[p] = '~' + l[p]
	s = ''.join(l)
	return s

def invert_symbols(s):
	match1 = re.search(r"[&]",s)
	match2 = re.search(r"[|]",s)
	if match1:
		ans = re.sub(r'[&]', '|', s)
		print '1 the exchange has been made %s' % ans
	elif match2:
		ans = re.sub(r'[|]', '&', s)
		print '2 the exchange has been made %s' % ans
	else:
		if random.randrange(0,2) == 1:
			ans = re.sub(r'[%]', '|', s)
			ans = add_tilde(re.split(r"(\W+)", ans), 2)
			print '3 the exchange has been made %s' % ans
		else:
			ans = re.sub(r'[%]', '&', s)
			ans = add_tilde(re.split(r"(\W+)", ans), 4)
			ans = re.sub(r'[<]', '~<', ans)
			print '4 the exchange has been made %s' % ans
			match3 = re.search(r"[~]{2}",ans)
			if match3:
				ans = re.sub(r'[~]{2}', '', ans)
				print '5 the exchange has been made %s' % ans
			return ans
	match4 = re.search(r"[~]{2}",ans)
	if match4:
		ans = re.sub(r'[~]{2}', '', ans)
		print '6 the exchange has been made %s' % ans
	match5 = re.search(r"<~.'*..'*>",ans)
	if match5:
		ans = re.sub(r"[~]", "", ans)
		ans = add_tilde(re.split(r"(\W+)", ans), 4)
		ans = re.sub(r'[<]', '~<', ans)
		print '7 the exchange has been made %s' % ans
		return ans
	match6 = re.search(r"<.'*.~.'*>",ans)
	if match6:
		ans = re.sub(r"[~]", "", ans)
		ans = add_tilde(re.split(r"(\W+)", ans), 2)
		ans = re.sub(r'[<]', '~<', ans)
		print '8 the exchange has been made %s' % ans
		return ans
	match7 = re.search(r"<~.'*.~.'*>",ans)
	if match7:
		ans = re.sub(r"[~]", "", ans)
		ans = re.sub(r'[<]', '~<', ans)
		print '9 the exchange has been made %s' % ans
		return ans
	match8 = re.search(r"<.'*..'*>",ans)
	if match8:
		ans = re.sub(r"[~]", "", ans)
		ans = add_tilde(re.split(r"(\W+)", ans), 2)
		ans = add_tilde(re.split(r"(\W+)", ans), 4)
		ans = re.sub(r'[<]', '~<', ans)
		print '10 the exchange has been made %s' % ans
		return ans

reg = markers_connectors(
	tilde(
		prime(
			atoms()
			)
		),
	markers_connectors(
		tilde(
			prime(
				atoms()
				)
			),
		markers_connectors(
			prime(
				tilde(
					atoms()
					)
				),
			tilde(
				prime(
					atoms()
					)
				)
			)
		)
	)

print atoms_values
check_regex(reg)
calculate(reg)
fantasy_rule(reg)
print atoms_values