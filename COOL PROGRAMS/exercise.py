def suma(a,b):
   return a+b

def resta(a,b):
   return a-b

def multi(a,b):
   return a*b

def divide(a,b):
   return 1.0 * a/b

def eleva(a,b):
   return a^b

dop = {'+': suma,'-': resta,'*':multi,'/':divide,'^':eleva}

######################################################################

a = int(raw_input('dame primer numero: '))
b = int(raw_input('dame el segundo numero: '))
o = raw_input('dame el operador [+ - * / ^]: ')

operacion = dop[o]

print ('%i %s %i = %i') % (a,o,b,operacion(a,b))