#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from random import shuffle


def set_rotors(r,k):
	if r[0] == k:
		return r
	else:
		r.append(r.pop(0))
		return set_rotors(r,k)

def clockwise_rotation(r):
	r.append(r.pop(0))
	print r
	return r

def counterclockwise_rotation(r):
	r.insert(0,r.pop())
	print r
	return r

def key_code(rI,rII,rIII):
	a = rI[random.randrange(1,26)]
	b = rII[random.randrange(1,25)]
	c = rIII[random.randrange(1,24)]
	res = [a,b,c]
	return res

def switcheroo_pairs():
	r = alphabet
	while len(switcheroos) <= 9:
		s1 = r.pop(random.randrange(1,len(r)))
		s2 = r.pop(random.randrange(1,len(r)))
		switcheroos.append((s1,s2))
	print switcheroos
	return switcheroos

def start_enigma(r):
	p1 = random.randrange(0,5)
	p2 = random.randrange(0,4)
	p3 = random.randrange(0,3)
	r1 = r.pop(p1)
	r2 = r.pop(p2)
	r3 = r.pop(p3)
	print 'Rotors selected are:'
	print 'Rotor %i %s' % (p1,r1)
	print 'Rotor %i %s' % (p2,r2)
	print 'Rotor %i %s' % (p3,r3)
	kc = key_code(r1,r2,r3)
	print 'The code to start with is %s' % kc
	r1 = set_rotors(r1,kc[0])
	r2 = set_rotors(r2,kc[1])
	r3 = set_rotors(r3,kc[2])
	print 'Rotor %i ready %s' % (p1,r1)
	print 'Rotor %i ready %s' % (p2,r2)
	print 'Rotor %i ready %s' % (p3,r3)
	print [item for item in r1 if item[0] in kc[0]]
	print [item for item in r2 if item[0] in kc[1]]
	print [item for item in r3 if item[0] in kc[2]]
	print [r1,r2,r3],kc
	return [r1,r2,r3],kc

def execute_enigma(s,r,sw):
	k1 = r[0][0]
	k2 = r[1][0]
	k3 = r[2][0]
	r1 = r[0]
	r2 = r[1]
	r3 = r[2]
	fsw = ''
	print 'Key is %s,%s,%s' % (k1,k2,k3)
	encrypt = list(s)
	ans = []
	for i in encrypt:
		lr1 = r1[[item for item in r1 if i == item[0]][0][1]-1]
		print '%s becomes %s in rotor 1' % (i,lr1[0])
		clockwise_rotation(r1)
		if r1[0] == k1:
			clockwise_rotation(r2)
			if r2[0] == k2:
				clockwise_rotation(r3)
		lr2 = r2[lr1[1]-1]
		print '%s becomes %s in rotor 2' % (lr1[0],lr2[0])
		lr3 = r3[lr2[1]-1]
		print '%s becomes %s in rotor 3' % (lr2[0],lr3[0])
		clockwise_rotation(r1)
		if r1[0] == k1:
			clockwise_rotation(r2)
			if r2[0] == k2:
				clockwise_rotation(r3)
		lr4 = r3[lr3[1]-1]
		print '%s becomes %s in rotor 3' % (lr3[0],lr4[0])
		lr3 = r2[lr4[1]-1]
		print '%s becomes %s in rotor 2' % (lr4[0],lr3[0])
		lr2 = r1[lr3[1]-1]
		print '%s becomes %s in rotor 1' % (lr3[0],lr2[0])
		for j in sw:
			if j[0] == lr2[0]:
				fsw = j[1]
			elif j[1] == lr2[0]:
				fsw = j[0]
		if fsw != '':
			ans.append(fsw)
			print 'Switcheroo found, %s becomes %s' % (lr2[0],fsw)
			fsw = ''
		else:
			ans.append(lr2[0])
			print 'No switcheroo found for %s' % lr2[0]
	ans = ''.join(ans)
	print ans
	return ans

if __name__ == "__main__":
	alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	rotors = []
	switcheroos = []
	rotors_settled = []
	for i in range(1,6):
		rotor = []
		lets = []
		nums = []
		shuffle(alphabet)
		for j in alphabet:
			num = alphabet.index(j)+1
			let_num = (j, num)
			rotor = rotor + [let_num]
			rotor = sorted(rotor, key=lambda x: x[0])
		rotors = rotors + [rotor]
		print 'Rotor %i %s' % (i,rotor)
	sp = switcheroo_pairs()
	print 'Switched letters %s, %i' % (sp,len(sp))
	info = start_enigma(rotors)
	rotors_ready = info[0]
	key = info[1]
	secret = 'ALANTURING'
	print 'Secret messege %s' % secret
	print 'Rotors ready %s' % rotors_ready
	encrypted = execute_enigma(secret,rotors_ready,switcheroos)
	print 'Messege %s became %s' % (secret,encrypted)
	print 'Now to see if we can decode the bitch!!!!'
	for i,j in zip(rotors_ready,key):
		rotors_settled.append(set_rotors(i,j))
	secret = execute_enigma(encrypted,rotors_ready,switcheroos)
	print 'Secret messege %s was %s' % (encrypted,secret)

a = '00'
b = '12'
print a[0:1]
print a[0:1]+b
print a
print len(a)