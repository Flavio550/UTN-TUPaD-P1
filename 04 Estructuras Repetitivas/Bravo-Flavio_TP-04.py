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
for i in range (valor1+1 ,valor2) :
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
