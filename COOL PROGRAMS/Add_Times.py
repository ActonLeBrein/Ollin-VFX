# Alan Badillo Salas badillo.soft@hotmail.com
# 7 de febrero de 2015

# Ejercicio opcional 3: Expresiones booleanas

# Este ejercicio lleva un  nivel avanzado asi que ponga atencion a cada
# una de las instrucciones comentadas

# Descripcion del algoritmo
# 1. Guardar una cadena que es una expresion booleana en una variable
# 2. Limpiar la expresion de espacios blancos
# 3. Obtener la posicion del primer operador encontrado,
#   a partir de cierta posicion establecida
# 4. Comparar los operandos de izquierda y derecha al operador
#   4.1 Si los operandos son iguales entonces simplificamos la expresion
# 5. Devolver la expresion simplificada

# Ejemplo 1: a + A -> 1
# Ejemplo 2: A + A -> A
# Ejemplo 3: A + b -> A + b
# Ejemplo 4: a * a -> a
# Ejemplo 5: a * A * B -> 0 * B -> 0
# Ejemplo 6: A + a * b -> 1 * b -> b

# Observe que no hay precedencia de operadores, es decir
# no se tomara en cuenta si se debe hacer antes la multiplicacion que la suma
# siempre se hara de izquierda a derecha sin importar el operador
# mas adelante resolveremos la precedencia de operadores

#################################################################################

# Esta funcion copia la expresion sin los espacios blancos y devuelve la copia
def quitar_blancos(expresion):
    # Creamos la expresion copia
    expresion2 = ''
    
    # Recorremos cada caracter de la expresion
    # Observe que la expresion es equivalente a una lista de caracteres
    i = 0
    while i < len(expresion):
        # Si el caracter no es (!=) espacio blanco, copiamos el caracter
        # en la expresion copia
        if expresion[i] != ' ':
            expresion2 += expresion[i]
        
        # Incrementamos el contador de posiciones
        i += 1
    
    # Devolvemos la expresion copiada sin los caracteres blancos
    return expresion2

# Creamos una tupla con los posibles operadores
operadores = ('+', '*')

# Obtenemos la primer primer posicion del operador
# a partir de pos
def pos_operador(expresion, pos):
    # Recorremos los caracteres de la expresion desde pos
    i = pos
    while i < len(expresion):
        # Contamos cuantas veces el caracter esta en la tupla de operadores
        # es decir, estamos viendo si el caracter esta en la tupla de operadores
        # es decir, preguntamos si el caracter es un operador
        if operadores.count(expresion[i]) > 0:
            # Devolvemos la posicion del operador
            return i
        
        i += 1
    
    # Si no encontramos ningun caracter operador en la expresion devolvemos -1
    return -1

# Simplificamos la expresion en el operador con posicion tal
def simplificar(expresion, pos_op):
    # Si el operador esta en un extremo entonces es una operacion no valida
    # por ejemplo A+b* o *a+B
    if pos_op - 1 < 0 or pos_op + 1 >= len(expresion):
        print "simplificar: Operacion invalida"
        # Devolvemos que no pudimos simplificar, luego las dos posiciones siguientes al
        # operador y la expresion sin modificacion
        return (False, pos_op + 2, expresion)
    
    # Obtenemos la variable (operando) del lado izquierdo al operador
    L = expresion[pos_op - 1]
    # Obtenemos el operador en la posicion pos_op
    op = expresion[pos_op]
    # Obtenemos la variable (operando) del lado derecho al operador
    R = expresion[pos_op + 1]
    
    # Opcionalmente imprimimos los operandos y el operador
    #print "[%s|%s|%s]" %(L, op, R)
    
    # Comprobamos si los operandos son la misma variable por ejemlo a y A
    # mediante la conversion a minusculas por ejemplo a y A -> a y a -> iguales
    # o si alguna variable es 0 o 1
    if L.lower() == R.lower() or \
        L == '0' or L == '1' or \
        R == '0' or R == '1':
        # Para el caso de la suma tenemos las siguientes restricciones
        if op == '+':
            if L == '0': # el caso 0+x -> x
                new = R
            elif R == '0': # el caso x+0 -> x
                new = L
            elif L == '1': # el caso 1+x -> x
                new = R
            elif R == '1': # x+1 caso x+1 -> x
                new = L
            elif L == R: # x+x -> x
                new = L
            else:
                new = '1' # x+X o X+x -> 1
        elif op == '*': # Similarmente para la multiplicacion
            if L == '0' or R == '0':
                new = '0'
            elif L == '1':
                new = R
            elif R == '1':
                new = L
            elif L == R:
                new = L
            else:
                new = '0'
        
        # Obtenemos una copia desde 0 hasta dos antes al operador
        # por ejemplo LLLLLLa+bRRRRRR -> LLLLLL
        expresionL = copiar(expresion, 0, pos_op - 2)
        # Obtenemos una copia desde dos despues al operador hasta el final
        # por ejemplo LLLLLLa+bRRRRRR -> RRRRRR
        expresionR = copiar(expresion, pos_op + 2, len(expresion) - 1)
        
        # Devolvemos que si pudimos simplificar y la nueva expresion
        return (True, pos_op + 2, expresionL + new + expresionR)
    
    # No pudimos simplificar
    return (False, pos_op + 2, expresion)

# Copiamos la expresion desde ini hasta fin en una nueva y la devolvemos
def copiar(expresion, ini, fin):
    expresion2 = ''
    
    i = ini
    while i <= fin:
        expresion2 += expresion[i]
        i += 1
        
    return expresion2

#################################################################################

# 1. Leemos la expresion dada por el usuario
expresion = raw_input("Ingresa una expresion booleana:> ")

# 2. Quitamos los blancos
expresion = quitar_blancos(expresion)

print "La expresion es: [%s]" %expresion

# Marcamos como que tenemos que simplificar
simplificada = True

# Iteramos mientras tengamos que simplificar
pos = 0
while simplificada:
    # 3. Obtenemos la posicion del primer operador
    pos_op = pos_operador(expresion, pos)
    
    # Si no hay mas operadores terminamos
    if pos_op == -1:
        print "No hay mas operadores, ya no se puede simplificar mas"
        print "Final: [%s]" %expresion
        # Rompemos el ciclo
        break
        
    # 4. Intentamos simplificar en el operador encontrado
    (simplificada, pos, expresion) = simplificar(expresion, pos_op)
    
    # Si pudimos simplificar volvemos a empezar, reiniciamos la posicion
    if simplificada:
        pos = 0
        
    # Si aun no recorremos toda la expresion entonces seguimos simplificando
    if pos < len(expresion):
        simplificada = True

    print "Simplificada: [%s]" %expresion