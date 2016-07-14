def AtoI(st):
	num = list(st)
	integers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	total = 0
	neg = False
	power = len(num) - 1
	for i in num:
		if i == '-':
			neg = True
			power -= 1
		elif i in integers:
			total = total + (int(i) * (10**power))
			power -= 1
		else:
			total = 0
			break
	if neg:
		total = list(str(total))
		total.reverse()
		total = ''.join(total)
		total = int(total)
	return total

print AtoI('-123456785521189')
print AtoI('-fgd')