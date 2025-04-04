# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
Edad = int(input ("ingrese su edad"))
if Edad > 18 :
     print ("Es mayor de edad")
else: 
     print ("no es mayor de edad")       


#2)Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
# mensaje “Desaprobado”
Nota = float(input ("ingrese su nota"))
if Nota >= 6 : 
     print ("aprovado")
else:
     print ("desaprobado")

#3)Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
#operador de módulo (%) en Python para evaluar si un número es par o impar.   
numero = int (input("ingrese un numero par"))
if numero % 2 == 0 :
        print ("ha ingresado un numero par")
else :
        print ("por favor, ingrese un numero par") 

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
# siguientes categorías pertenece: 
# Niño/a: menor de 12 años. 
# Adolescente: mayor o igual que 12 años y menor que 18 años. 
# Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# Adulto/a: mayor o igual que 30 año        
Edad_usuario = int(input("ingrese su edad")) 
if Edad_usuario < 12 :
      print ("niño/a")   
elif Edad_usuario >= 12 and Edad_usuario < 18 :
      print ("adolecente")    
elif Edad_usuario >= 18 and Edad_usuario < 30 :
      print ("adulto/a")      
else : 
     print ("adulto")      

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
#como una lista o un string. 
contraseña = input("ingrese una contraseña")
if 8 <= len(contraseña) <= 14 : 
      print ("ha ingresado una contraseña correcta")
else :
      print ("por favor, ingrese una contraseña de entre 8 y 14 caracteres ") 

#6) Escribir un programa que tome la lista 
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.     
import random
from statistics import mode, median, mean
#se genera una lista aleatoria de 50 numeros entre 1 y 100)
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode (numeros_aleatorios)
mediana = median (numeros_aleatorios)
media = mean (numeros_aleatorios)
#Determinar sesgo
if media > mediana > moda:
      print ("sesgo positivo (a la derecha)")
elif media < mediana < moda :
      print ("sesgo negativo (a la izquierda)")
else :
      print ("no hay sesgo") 

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
#pantalla.
Palabra_frase = input ("ingrese una palabra o frase")            
vocales = "aeiouAEIOU"
if Palabra_frase and Palabra_frase [-1] in vocales :
      print ("!")
print ("Resultado :", Palabra_frase)


      
