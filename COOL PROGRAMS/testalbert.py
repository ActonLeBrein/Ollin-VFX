valor = input('give me  a number please?    ')
total = (valor * 2) - 1

for row in range(0,valor):
    a = [' ']*(total)
    l = valor - row
    r = valor + row
    a[l-1]= '*'
    a[r-1] = '*'
    print ''.join(a)

row = 1
while row < valor:
    a = [' ']*(total)
    l = row
    r = total - row
    a[l] = '*'
    a[r-1] = '*'
    print ''.join(a)
    row += 1
    
for row in range(0,valor):
    a = [' ']*(total)
    if row == 0:
        a[valor-1] = '*'
    else:
        l = valor - row
        r = valor + row
        for i in range(l,r):
            a[i]= '*'
    print ''.join(a)
    
row = 1
while row < valor:
    a = [' ']*(total)
    l = row + 1
    r = total - row + 1
    for i in range(l,r):
        a[i] = '*'
    print ''.join(a)
    row += 1

valor = input('give me  a number please?    ')
total = (valor * 2) - 1

for row in range(0,valor):
    a = [' ']*(total)
    l = valor - row
    r = valor + row
    a[l-1]= '*'
    a[r-1] = '*'
    print ''.join(a)
    
for row in reversed(range(0,valor-1)):
    a = [' ']*(total)
    l = valor - row
    r = valor + row
    a[l-1]= '*'
    a[r-1] = '*'
    print ''.join(a)