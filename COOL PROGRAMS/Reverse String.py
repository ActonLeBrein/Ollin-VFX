def Reverse_String(st):
	sent = st.split()
	for i in range(len(sent)):
		rev = list(sent[i])
		rev.reverse()
		sent[i] = ''.join(rev)
	sent.reverse()
	return sent

print Reverse_String('HELLO MOTO BITCHES!!!!')