import math

phi_pos = (1+math.sqrt(5)) / 2
phi_neg = (1-math.sqrt(5)) / 2
phi = phi_pos**3
psi = phi_neg**3

def Fib_Num(n):
    return int(round(((1+math.sqrt(5))**n-(1-math.sqrt(5))**n)//(2**n*math.sqrt(5))))

def Fib_Inv(n):
    return int(round((math.log(n*(math.sqrt(5))) / math.log(phi_pos))))

def Fib_Inv_Log1(n):
    return int(round(math.log((Fib_Num(n)*math.sqrt(5) + math.sqrt(5*(Fib_Num(n)**2)+4))/2,phi_pos)))

def Fib_Inv_Log2(n):
    return int(round(math.log((n*math.sqrt(5) + math.sqrt(5*(n**2)+4))/2,phi_pos)))

def Fib_Even(k):
    return int(round((1/math.sqrt(5)) * ((phi * ((1 - phi**k) / (1 - phi))) + (psi * ((1 - psi**k) / (1 - psi))))))

print 'Fib_Even is {}\n'.format(Fib_Even(10))

sum_t = 0
i = 1
while i <= 30:
    print 'i is {}'.format(i)
    if i%3 == 0:
        sum_t = sum_t + Fib_Num(i)
    elif i%3 == 1:
        print '{0} {1}'.format(i,i-1)
    elif i%3 == 2:
        print '{0} {1}'.format(i,i-2)
    else:
        pass
    print 'Fib_Num is {}'.format(Fib_Num(i))
    print 'Fib_Inv is {}'.format(Fib_Inv(Fib_Num(i)))
    print 'Fib_Inv_Log is {}'.format(Fib_Inv_Log1(i))
    print '{} is near to fib num {}'.format(i,Fib_Inv(i))
    print '{} is near to fib num {}\n'.format(i,Fib_Inv_Log2(i))
    i = i + 1
print sum_t
print sum_t == Fib_Even(10)