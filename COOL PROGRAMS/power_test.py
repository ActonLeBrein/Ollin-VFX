def pow1(x,y):
    a = x
    i = 0
    if y == 0:
        return 1
    else:
        while i < y:
            a = a * x
            i += 1
        return a
        
def pow2(x,y):
    if y == 0:
        return 1
    else:
        return x * pow2(x,y-1)

def pow3(x,y):
    if y == 0:
        return 1
    a = pow2(x,y/2)
    elif y%2 == 0:
        return a * a    
    else:
        return a * a * x