# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# -Naranja = 1200
# -Manzana = 1500
# -Pera = 2300
precio_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
# Agregamos las siguientes frutas con sus precios al diccionario:
precio_frutas ['Naranja'] = 1200 
precio_frutas ['Manzana'] = 1500
precio_frutas ['Pera'] = 2300

print (precio_frutas)

#/////////////////////////////////////////////////////////////

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# Banana = 1330
# Manzana = 1700
# Melón = 2800
precio_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera' : 2300 } 
# Actualizamos los precios requeridos :
precio_frutas ['Banana'] = 1330
precio_frutas ['Manzana'] = 1700
precio_frutas ['Melon'] = 2800

print(precio_frutas)

#///////////////////////////////////////////////////////////////

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.
precio_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera' : 2300 }
# Creamos la lista de frutas:
list(precio_frutas)
precio_frutas = ["banana", "Anana", "Melon", "Uva", "Naranja", "Manzana", "Pera"]
print(precio_frutas)

#////////////////////////////////////////////////////////////////

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# luego, pedí un nombre y mostrale el número asociado, si existe.
Contactos = {}
# Bucle for para iterar 5 veces y obtener los 5 contactos y sus numeros
for i in range (5):
    nombre = input(f"ingrese el nombre del contacto {i + 1} :")
    numero = input(f"ingrese el numero de {nombre} : ")
    Contactos[nombre] = numero
# Consultamos si el nombre ingresado esta en los contactos. Si esta se imprime el numero del nombre ingresado,
#  sino es porque ese nombre no esta en el diccionario
consulta = input("ingresa un nombre de un contacto")
if consulta in Contactos:
    print(f"el numero asociado del nombre ingresado es : {Contactos[consulta]}")
else:
    print("el nombre no esta en los cantactos")

#///////////////////////////////////////////////////////////////////

# 5) Solicita al usuario una frase e imprime:
# Las palabras únicas (usando un set).
# Un diccionario con la cantidad de veces que aparece cada palabra.
Frase = input("ingrese una frase")

Palabras = Frase.split()
#Usamos un set para tener palabras unicas 
palabras_unicas = set(Palabras)
print(f"palabras unicas : {palabras_unicas}")

Dic_palabras_unicas = {}
for palabra in Frase :
    if palabra in Dic_palabras_unicas :
        Dic_palabras_unicas[palabra] += 1
    else:
        Dic_palabras_unicas = 1

print("\nFrecuencia de cada palabra:")
for palabra, cantidad in Dic_palabras_unicas.items():
    print(f"{palabra}: {cantidad}" )       

#//////////////////////////////////////////////////////////

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.
Notas_Alumnos = {}
# bucle que se repite 3 veces para completar las 3 notas de los 3 estudiantes
for i in range (3):
    nombre = input(f"ingrese el nombre del alumno {i+1}:")
    print(f"Ingresá las 3 notas de {nombre}:")
    
    # Pedir tres notas y convertirlas en una tupla
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    Notas_Alumnos[nombre] = (nota1, nota2, nota3)
# Mostramos el promedio de cada alumnno
print("Promedios:")
for nombre, notas in Notas_Alumnos.items():
    promedio = sum(notas) / 3
    print(f"{nombre}: {promedio:.2f}")    

#///////////////////////////////////////////////////////////////

#6) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# Mostrá los que aprobaron ambos parciales.
# Mostrá los que aprobaron solo uno de los dos.
# Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
# Conjuntos de estudiantes que aprobaron cada parcial
parcial1 = {"FLAVIO", "PEDRO", "ANA", "MERLINA", "BELLON", "CARLOS"}
parcial2 = {"FLAVIO", "JOSE", "ANA", "JESICA", "MERLINA", "EITHAN"}
# Estudiantes que aprobaron ambos parciales (intersección)
ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

# Estudiantes que aprobaron solo uno de los dos (diferencia simétrica)
solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los dos:", solo_uno)

# Estudiantes que aprobaron al menos uno (unión)
al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)

#///////////////////////////////////////////////////////////////

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# Consultar el stock de un producto ingresado.
# Agregar unidades al stock si el producto ya existe.
# Agregar un nuevo producto si no existe.

stock_productos = {"harina": 20,"aceite": 15,"fideos": 30}

# Mostrar el stock inicial
print("Stock inicial:")
for producto, cantidad in stock_productos.items():
    print(f"{producto}: {cantidad} unidades")

# Pedir producto al usuario
producto = input("\nIngresá el nombre del producto que querés consultar o modificar: ").lower()

# Consultar si existe
if producto in stock_productos:
    print(f"Hay {stock_productos[producto]} unidades de '{producto}' en stock.")
    
    # Preguntar si quiere agregar más
    agregar = input("¿Querés agregar unidades a este producto? (sí/no): ").lower()
    if agregar == "si":
        unidades = int(input("¿Cuántas unidades querés agregar?: "))
        stock_productos[producto] += unidades
        print(f"Nuevo stock de '{producto}': {stock_productos[producto]}")
else:
    # Si no existe, preguntar si quiere agregarlo
    print(f"'{producto}' no está en el stock.")
    agregar_nuevo = input("¿Querés agregar este nuevo producto? (sí/no): ").lower()
    if agregar_nuevo == "si":
        unidades = int(input("¿Cuántas unidades querés agregar?: "))
        stock_productos[producto] = unidades
        print(f"Producto '{producto}' agregado con {unidades} unidades.")

# Mostrar el stock actualizado
print("\nStock actualizado:")
for producto, cantidad in stock_productos.items():
    print(f"{producto}: {cantidad} unidades")

#///////////////////////////////////////////////////////////////////////////

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos
agenda = {("Lunes", "10:00"): "Reunión con equipo",("Martes", "14:30"): "Clase de Python",("Miércoles", "09:00"): "Gimnasio",("Jueves", "16:00"): "Dentista",("Viernes", "11:15"): "Entrega de informe"}

# Mostrar todos los eventos de la agenda
print("Agenda semanal:")
for clave, evento in agenda.items():
    dia, hora = clave
    print(f"{dia} a las {hora}: {evento}")

# Consultar un evento por día y hora
dia = input("\nIngresá un día para consultar (ej: Lunes): ").capitalize()
hora = input("Ingresá la hora (ej: 10:00): ")

clave = (dia, hora)

if clave in agenda:
    print(f"Evento encontrado: {agenda[clave]}")
else:
    print("No hay evento programado en ese día y hora.")     

#/////////////////////////////////////////////////////////////////////////////

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# Las capitales sean las claves.
# Los países sean los valores.
paises = {"Argentina": "Buenos Aires","Brasil": "Brasilia","Chile": "Santiago","Uruguay": "Montevideo","Paraguay": "Asunción"}

# Crear nuevo diccionario: capital , país
capitales = {}
for pais, capital in paises.items():
    capitales[capital] = pais

# Mostrar el nuevo diccionario
print("Diccionario invertido (capital -> país):")
for capital, pais in capitales.items():
    print(f"{capital}: {pais}")