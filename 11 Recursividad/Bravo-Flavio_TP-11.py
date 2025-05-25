# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
# función para calcular y mostrar en pantalla el factorial de todos los números enteros 
# entre 1 y el número que indique el usuario
def factorial(n):
    if n == 0 or n == 1: # Caso base: si n es 0 o 1, el factorial es 1
        return 1  
    else:
        return n * factorial(n - 1) # Se aplica la recursividad
n = int(input("ingrese un numero entero positivo para saber su factorial"))
print (f"el factorial de {n} es {factorial(n)}")

#////////////////////////////////////////////////////////////

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
# especifique. (la serie de Fibonacci es la sucesion de numeros donde cada numero es la suma de los dos anteriores)
def fibonacci(valor):
    if valor == 0:
        return 0    #caso base 1
    elif valor == 1:
        return 1    #caso base 2
    else:
        return fibonacci(valor - 1) + fibonacci(valor - 2)

posicion = int(input("ingrese hasta que posicion se va realizar la serie de Fibonacci"))
for i in range (posicion + 1): # va de 0 hasta la posicion inclusive
    print(f"fibonacci de {posicion} es {fibonacci(i)}") # imprime los resultados de la serie

#////////////////////////////////////////////////////////////////////

#3)Crea una función recursiva que calcule la potencia de un número base elevado a un 
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
# algoritmo general.
def potencia(base,exponente):
    if exponente == 0: # caso base
     return 1
    else:
       return base * potencia (base,exponente-1) # se Multiplicá la base por el resultado dado volver a llamar  
                                                   # a la función, pero con un exponente menor, hasta que exponente sea 0
n = int(input("ingrese la base"))   
m = int(input("ingrese el exponente")) 
resultado = potencia(n,m)
print (f"{n} elevado a la {m} da como resultado {resultado}")

#///////////////////////////////////////////////////////////////

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base 
# decimal y devuelva su representación en binario como una cadena de texto. 
def decimal_a_binario (numero):
    if numero == 0: 
        return "0"  #caso base
    else:
        return decimal_a_binario(numero // 2) + str(numero % 2) #funcion recursiva hasta llegar a 0
num = int(input("ingrese un numero entero decimal"))    
binario = decimal_a_binario (num)
print (f"el numero {num} en binario es {binario} ")

#////////////////////////////////////////////////////////////////   

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
#lo es. 
def es_palindromo(palabra, inicio=0, fin=None):
    if fin is None:
        fin = len(palabra) - 1

    if inicio >= fin:
        return True  # Caso base: se cruzaron, es palíndromo

    if palabra[inicio] != palabra[fin]:
        return False  # No coinciden las letras

    return es_palindromo(palabra, inicio + 1, fin - 1)  # Llamada recursiva

texto = input("Ingrese una palabra (sin espacios ni tildes): ").lower()
if es_palindromo(texto):
    print(f'"{texto}" es un palíndromo.')
else:
    print(f'"{texto}" no es un palíndromo.')

#////////////////////////////////////////////////////////////

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
#número entero positivo y devuelva la suma de todos sus dígitos. 
#     Restricciones: 
#No se puede convertir el número a string. 
#Usá operaciones matemáticas (%, //) y recursión. 
#Ejemplos: 
#suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
#suma_digitos(9)      → 9 
#suma_digitos(305)    → 8   (3 + 0 + 5) 
def suma_digitos(numero) :
    if numero < 10 :
        return numero # caso base: un solo digito. ejemplo: 8 = 8
    else :
        return (numero % 10) + suma_digitos (numero // 10) #llamada recursiva

Entero_positivo = int(input("ingrese un numero entero positivo"))    
suma = suma_digitos(Entero_positivo)
print(f"la suma de todos los digitos de {Entero_positivo} es {suma}")

#///////////////////////////////////////////////////////////////////

#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
#último nivel con un solo bloque. 
 
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
#pirámide. 
#Ejemplos: 
#contar_bloques(1)   → 1  (1) 
#contar_bloques(2)   → 3  (2 + 1) 
#contar_bloques(4)   → 10 (4 + 3 + 2 + 1) 
def contar_bloques(bloques):
    if bloques == 1:
        return 1 # caso base, no hay bloques para contar por que solo se ingreso 1 bloque
    else:
        return bloques + contar_bloques(bloques-1) # llamada recursiva, la cantidad de bloques decrece en 1 hasta llegar a 0
bloques_bajo_nivel = int(input("ingrese el numero de bloques del nivel mas bajo(el inicial)"))
total_bloques = contar_bloques(bloques_bajo_nivel)
print(f"la cantidad necesaria que se necesita para armar la piramide es de {total_bloques} bloques")

#/////////////////////////////////////////////////////////////////////////////////////////////

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
#aparece ese dígito dentro del número. 
#Ejemplos: 
#contar_digito(12233421, 2) → 3   
#contar_digito(5555, 5)     → 4
def contar_digito(numero,digito):
    if numero < 10:
        return 1    #caso base 1, si el menor a 10, no hay repeticion de digitos 
    elif numero == digito:   
        return 0    #caso base 2, no hay repeticion de digito yan que es el mismo que el numero
    else:
        ultimo = numero % 10
        if ultimo == digito:
            cuenta = 1
        else: cuenta = 0
    return cuenta + contar_digito(numero // 10, digito) #llamada recursiva
num = int(input("ingrese un numero entero positivo"))
dig = int(input("ingrese un digito entre 0 y 9"))
resultado = contar_digito(num, dig)
print(f"El dígito {dig} aparece {resultado} veces en {num}.")