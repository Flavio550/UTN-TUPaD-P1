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

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
#dependiendo de la opción que desee: 
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.
# upper : convierte todas las letras de un string a mayusculas
#lower : Convierte todas las letras de un string a minusculas
#title : Convierte la primera letra de un string a mayusculas y las demas a minusculas
Nombre = (input("ingrese su nombre"))
print ("ingrese el numero dependiendo la opcion que desee")
print ("1, si quiere su nombre en mayusculas")
print ("2, si quiere su nombre en minusculas")
print ("3, si quiere la primera letra en mayusculas y despues las demas en minusculas")
opcion = int  (input ("ingrese el numero elegido"))
if opcion == 1:
      print (Nombre.upper())
elif opcion == 2:
      print (Nombre.lower())      
elif opcion == 3:
      print (Nombre())    
else:
      print ("opcion no valida, elija el numero 1,2 o 3")  

#  9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
#por pantalla: 
#● Menor que 3: "Muy leve" (imperceptible). 
#● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
#generalmente no causa daños). 
#● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
#débiles). 
#● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).     
Magnitud = int (input ("ingrese la magnitud de un terremoto"))
if Magnitud < 3 :
      print ("muy leve, (inperseptible)")
elif Magnitud <= 3 and Magnitud < 4 :
      print ("leve,ligeramente perseptible")  
elif Magnitud >= 4 and Magnitud < 5 :
      print ("moderaro,(sentido por personas, pero mo causa daños)")  
elif Magnitud >= 5 and Magnitud < 6 :
      print ("fuerte, (puede causar daños en estructuras debiles )")     
elif Magnitud >= 6 and Magnitud < 7 :
      print ("muy fuerte (puede causar daños significativos)")      
else :
      print ("Extremo(puede causar graves daños a gran escala)") 

#10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
#si el usuario se encuentra en otoño, invierno, primavera o verano.
hemisferio =  input ("en cual hemisferio se encuentra? (Norte=N, Sur=S):").upper()
mes = int (input("ingrese el numero del mes (1-12)"))
dia = int (input ("ingrese el dia del mes"))
#Determinamos la estacion segun el hemisferio
if (mes == 12 and dia >=21) or (mes in [1,2]) or (mes == 3 and dia <=20):
      estacion_norte = "inverno"
      estacion_sur = "verano"
elif (mes == 3 and dia >=21) or (mes in [4,5]) or (mes == 6 and dia <=20 ):
      estacion_norte = "primavera"
      estacion_sur = "otoño"
elif (mes == 6 and dia >=21) or (mes in [7,8]) or (mes == 9 and dia <=20):
      estacion_norte ="verano" 
      estacion_sur = "invierno"
else : #Desde el 21 de septiembre hasta el 20 de diciembre (incluidos)
      estacion_norte = "otoño"
      estacion_norte = "primavera"
# Elegimos la estacion segun el hemisferio
if hemisferio == "N":
      estacion = estacion_norte
elif hemisferio == "S":
      estacion = estacion_sur
else:
      estacion = "hemisferio invalido, ingres N o S"   
print (f"estas en la estacion {estacion}")               