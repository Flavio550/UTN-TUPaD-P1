# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
Lista_multiplos_4 = list (range(4,101,4))
print (Lista_multiplos_4) 

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
#penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
#indexing con números negativos!
lista_5_elementos = [1,2.8,10,"Hola", True]
# se crea la variable para llamar al penultimo elemento de la lista creada.
penultimo_elemento = lista_5_elementos [3]
print (penultimo_elemento)

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla
lista_vacia = []
#Se agregan de a uno los elementos, ya que append agrega de un elemento a la vez
lista_vacia.append("HOLA")
lista_vacia.append("BIENVENIDOS")
lista_vacia.append("HASTA PRONTO")
print (lista_vacia) 

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
#respectivamente. Imprimir la lista resultante por pantalla.
lista_animales = ["perro","gato","foca","tucan","jirafa"]
print (lista_animales)
lista_animales [-4] = "loro"
lista_animales [-1] = "oso"
print (lista_animales)

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
# Se crea una lista de numeros de 5 elementos
numeros = [8,15,3,22,7]
# Se elimina el maximo numero de la lista, numero.remove(max(numeros)):se usa para eliminar un elemento de la lista,
# en este caso el maximo de los numeros, (max)
numeros.remove(max(numeros))
#Se imprimen los elementos de la lista, menos el que se elimino (elemento 3 = 22)
print(numeros)

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros
numeros_10_al_30 = list(range(10,31,5))
primeros_dos = numeros_10_al_30 [0:2]
print(primeros_dos)

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
#cuales quiera. autos = ["sedan", "polo", "suran", "gol"]
modelo_autos = ["sedan", "polo", "suran", "gol"]
modelo_autos [1] = "fox"
modelo_autos [2] = "tiguan"
print(modelo_autos)

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla.
# Se crea la lista vacia
dobles = []
# Se agregan de a uno el doble de los elementos pedidos usando append
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles) 

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
#diferentes clientes: (ejercicio de listas anidadas)
#compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla
#/// lista con 3 sublistas. 0, 1 y 2
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]] 
# a: se agrega jugo a la sublista [2]
compras[2].append("jugo")
# b: se reemplaza fideos por tallarines en la sublista [1]
compras[1][1] = "tallarines"
# c: se elimina pan de la sublista [0]
compras[0].remove("pan")
# d: se imprime la lista resultante
print(compras)

#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# Posición lista_anidada[0]: 15
# Posición lista_anidada[1]: True
# Posición lista_anidada[2][0]: 25.5
# Posición lista_anidada[2][1]: 57.9
# Posición lista_anidada[2][2]: 30.6
# Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.
lista_anidada = [[15],[True],[25.5 , 57.9 , 30,6],[False]]
print(lista_anidada)


