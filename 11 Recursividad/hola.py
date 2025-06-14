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