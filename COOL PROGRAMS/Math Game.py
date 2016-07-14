def math_game(num,lis):
	seq = [4,2,1]
	final = False
	if len(lis) > len(seq):
		for i in range(len(lis)):
			if lis[i:i+len(seq)] == seq:
				final = True
		if final:
			print 'Final result is %s' % lis
			print 'Number of times done %s' % len(lis)
		else:
			if num%2 == 1:
				lis.append((num*3)+1)
				math_game((num*3)+1,lis)
			else:
				lis.append(num/2)
				math_game(num/2,lis)
	else:
		if num%2 == 1:
			lis.append((num*3)+1)
			math_game((num*3)+1,lis)
		else:
			lis.append(num/2)
			math_game(num/2,lis)

math_game(12647384,[12647384])