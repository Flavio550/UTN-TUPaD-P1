# EJERCICIO 1
#//Se define la funcion 
def imprimir_hola_mundo ():
    print ("Hola Mundo")

#//Programa principal
Saludar = imprimir_hola_mundo () 

#///////////////////////////////////

# EJERCICIO 2
#//Se define funcion
def saludar_usuario(nombre):
    print (f"! Hola {nombre} !")

#//Programa principal
Saludo_personalizado = input ("ingrese su nombre")
saludo = saludar_usuario (Saludo_personalizado)

#///////////////////////////////////

# EJERCICIO 3
#//Se define funcion
def informacion_personal (mensaje1,mensaje2,mensaje3,mensaje4):
 return (mensaje1,mensaje2,mensaje3,mensaje4)

#//Programa principal
nombre = input ("ingrese su nombre")
apellido = input ("ingrese su apellido")
edad = input ("ingrese su edad")
residencia = input ("ingrese su residencia")
informacion_personal (nombre,apellido,edad,residencia)
print (f"soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#///////////////////////////////////

#EJERCICIO 4
#// Definicion de funciones 
def calcular_area_circulo(dato):
    return 3.14 * dato * dato

def calcular_perimetro_circulo(dato):   
    return 2 * 3.14 * dato

#// Programa principal    
radio = int (input ("ingrese el radio del circulo "))
area = calcular_area_circulo (radio)
perimetro = calcular_perimetro_circulo (radio)
print (f"El area del circulo es {area} y el perimetro es {perimetro}")

#//////////////////////////////////////

#Ejercicio 5 
#// Se definen las funciones 
def segundos_a_horas(segundos) :
 return segundos // 3600

#// Programa principal
segundos = int (input ("ingrese los segundos"))
horas = segundos_a_horas (segundos)
print (f"Los {segundos} segundos ingresados corresponden a {horas} horas ")

#/////////////////////////////////////  
    
# EJERCICIO 6
#// Se define funcion
def tabla_multiplicar (numero):
 for i in range (1,11) :
  resultado = numero * i
  print (resultado) 
 
#// Programa principal
numero = int (input("Ingrese un numero"))    
tabla = tabla_multiplicar (numero)

#////////////////////////////////////////

# EJERCICIO 7
#Se define la funcion 
def operaciones_basicas (a , b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b 
    division = a // b
    print (f"La suma entre {a} y {b} es {suma}")
    print (f"La resta entre {a} y {b} es {resta}")
    print (f"La multiplicacion entre {a} y {b} es {multiplicacion}")
    print (f"La division entre {a} y {b} es {division}")

#// Programa principal 
a = int (input("ingrese el primer numero")) 
b = int (input("ingrese el segundo numero")) 
Operaciones = operaciones_basicas (a , b)

#/////////////////////////////////////////

#EJERCICIO 8
#// Se define la funcion
def calcular_imc(peso, altura) :
   IMC = peso / (altura ** 2)
   print (f"el indice de masa corporal es {IMC}")

#// Programa principal 
Peso = float (input("ingrese su peso en kilogramos"))
Altura = float (input("ingrese su altura en metros"))
calcular_imc (Peso , Altura)

#//////////////////////////////////////////

# EJERCICIO 9 
#// Se define funcion
def celsius_a_fahrenheit(celsius):
    equivalencia = (celsius * 9/5) + 32  
    print (f"la temperatura en grados fahrenheit es {equivalencia}")

#// Programa principal
temperatura = int (input("ingrese la temperatura en grados celsius"))    
celsius_a_fahrenheit (temperatura)

#//////////////////////////////////////////

# EJERCICIO 10
#// Se define funcion
def calcular_promedio (a,b,c):
    return (a + b + c) // 3

#// Programa principal
a = int (input("ingrese un numero")) 
b = int (input("ingrese un numero")) 
c = int (input("ingrese un numero")) 
promedio = calcular_promedio (a,b,c)
print (f"el promedio de {a}, {b} y {c} es {promedio}")

#///////////////////////////////////////////////////////
