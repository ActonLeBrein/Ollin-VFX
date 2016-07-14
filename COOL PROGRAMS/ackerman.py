def ack(m,n):
	if m == 0:
		return n + 1
	elif n == 0:
		return ack(m-1,1)
	else:
		return ack(m-1, ack(m,n-1))

i = 0
while (i < 6):
	j = 0
	while (j < 6):
		print 'ackerman (%i,%i) is: %i' % (i,j,ack(i,j))
		j += 1
	i += 1