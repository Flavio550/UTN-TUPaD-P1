#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for num in range (101):
     print (num)


#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.
num = int (input("ingrese un numero entero"))
cont = 0              #-iniciamos la variable cont para que comience a contar desde 0
while num > 0 :       #-usamos la estructura while para que el bucle se repita hasta que el num sea menor que 0                            
    cont += 1         #-contador comienza a contar y ya vale 1 
    num = num // 10   #-dividimos el numero por 10, todas las veces necesarias hasta que sea menor que 0 
print (f"el numero entero ingresado tiene {cont}")


#3)Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
valor1 = int (input("ingrese el primer valor"))
valor2 = int (input("ingrese el segundo valor"))
suma = 0
for i in range (valor1 + 1 , valor2) :
    suma += i
print (f"la suma de los numeros entre {valor1} y {valor2} es {suma}")  


#4)Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
numero = int (input("ingrese numeros enteros, y para terminar ingrese 0"))
total = 0 
while numero != 0 : #numero distinto a cero
    total += numero  #sumamos el total + el numero ingresado
    numero = int (input("ingrese otro numero o 0 para terminar"))  #se pide ingresar otro numero para repetir el bucle y asi ir sumando 
print (f"la suma de los numeros ingresados es {total}") # si seleccionamos 0, se termina la instruccion y se imprime la suma de los numeros ingresados              


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
aleatorio = random.randint(0 , 9) # se genera un numero aleatorio entre 0 y 9
num = int (input("ingrese un numero del 0 al 9"))
total = 1 # ya se hizo 1 intento, porque se ingreso un numero
while num != aleatorio : # se va a ejecutar el programa hasta que la variable num sea igual a la variable aleatorio
 num = int (input ("siga intentando")) # si el numero no es igual al aleatorio se sigue itentando
 total += 1 # se cuentan los intentos, para despiues mostrar por pantalla.
print (f"el total de intentos para acertar el numero fue de {total} intentos ")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente. 
pares = int,input #definimos la variable pares como enteros
for pares in range (100, 0 , -2) : #utilizamos for para que el bucle se repita desde 100 hasta 0, de dos en dos
    print (pares)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#   número entero positivo indicado por el usuario. 
num = int(input("ingrese un numero entero positivo"))
suma = 0 #iniciamos la variable suma en 0 para comezar a sumar desde 0
for i in range (0 , num +1):#usamos for para ir desde 0 al numero elegido y le sumamos 1 para incluirlo
    suma += i    #sumamos los numeros hasta que termine el bucle
print (f"la suma de todos los numero comprendidos entre 0 y el {num} es {suma}") #imprimimos el resultado de la suma 


#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#   programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#   negativos y cuántos son positivos. 

cantidad = 0 #se inician las variales en 0 para ir contandolas
pares = 0
impares = 0
positivos = 0
negativos = 0
# Se repite el bucle mientras la cantidad de numeros ingresada sea menor a 100.
while cantidad < 100 : 
    num = int(input("ingrese un numero entero:"))
    # usamos condicionales para los numeros que van ingresando y si son pares, impares, positivos o positivos, se van sumando
    if num % 2 == 0 :
        pares += 1
    else :
        impares += 1
    if num > 0 :
        positivos += 1
    else :
        negativos += 1
# se va sumando la cantidad de numeros ingresados
    cantidad += 1
    #se imprime la cantidad de numeros pares, impares, positivos y negativos.
print (f"cantidad de pares {pares}")
print (f"cantidad de impares {impares}")
print (f"cantidad de positivos {positivos}")
print (f"cantidad de negativos {negativos}")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
    #media de esos valores.

#Iniciamos las variables en 0
cantidad = 0 
sumatoria = 0
#Mientras la cantidad de numeros sea menor que 100, se va a repetir el bucle
while cantidad < 5 :
    num =int(input("ingrese un numero entero")) #se ingresa un numero
    sumatoria += num #Por cada ciclo, se van sumando los numeros ingresados
    cantidad +=1     # Se va contando la cantidad de los numeros ingresados hasta llegar a 100 veces
print (f"la media de los valores es {sumatoria / cantidad}") #Se imprime el valor de la media de todos los numeros sumados entre si
                                                             # dividido la cantidad de numeros ingresados que es 100.

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#     usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 
num = int (input("ingrese un numero"))
invertido = 0
while num > 0 :
    digito = num % 10
    invertido = (invertido * 10) + digito
    num = num // 10
print (f"numero invertido es : {invertido}")                                                             