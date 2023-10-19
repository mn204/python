'''
Métodos de las listas

Las listas tienen una serie de métodos que se pueden usar para manipularlas. Algunos de los métodos más comunes son:

* append(): Agrega un elemento a la lista al final.
* clear(): Elimina todos los elementos de la lista.
* copy(): Devuelve una copia de la lista.
* count(): Cuenta el número de veces que aparece un elemento en la lista.
* extend(): Agrega los elementos de una lista a otra lista.
* index(): Devuelve el índice del primer elemento que coincide con un valor dado.
* insert(): Inserta un elemento en la lista en un índice dado.
* pop(): Elimina el elemento de la lista en un índice dado.
* remove(): Elimina el primer elemento que coincide con un valor dado.
* reverse(): Invierte el orden de los elementos de la lista.
* sort(): Ordena los elementos de la lista.

'''
# Agregar un elemento al final de una lista
lista = ["a", "b", "c"]
lista.append("d")
print(lista)
# ["a", "b", "c", "d"]

# Eliminar el primer elemento de una lista
lista = ["a", "b", "c"]
lista.pop(0)
print(lista)
# ["b", "c"]

# Contar el número de veces que aparece un elemento en una lista
lista = ["a", "b", "c", "a", "b"]
print(lista.count("a"))
# 2

# Obtener el índice de un elemento en una lista
lista = ["a", "b", "c", "d"]
print(lista.index("c"))
# 2

# Insertar un elemento en una lista en un índice dado
lista = ["a", "b", "c"]
lista.insert(1, "x")
print(lista)
# ["a", "x", "b", "c"]

# Eliminar el primer elemento que coincide con un valor dado
lista = ["a", "b", "c", "d"]
lista.remove("a")
print(lista)
# ["b", "c", "d"]

# Invertir el orden de los elementos de una lista
lista = ["a", "b", "c", "d"]
lista.reverse()
print(lista)
# ["d", "c", "b", "a"]

# Ordenar los elementos de una lista
lista = ["c", "a", "b", "d"]
lista.sort()
print(lista)
# ["a", "b", c", "d"]
'''


Métodos de los diccionarios

Los diccionarios tienen una serie de métodos que se pueden usar para manipularlos. Algunos de los métodos más comunes son:

* clear(): Elimina todos los elementos del diccionario.
* copy(): Devuelve una copia del diccionario.
* get(): Devuelve el valor asociado a una clave, o un valor por defecto si la clave no existe.
* items(): Devuelve una lista de pares (clave, valor).
* keys(): Devuelve una lista de claves.
* pop(): Elimina el elemento asociado a una clave, y devuelve el valor.
* update(): Agrega o actualiza los elementos de un diccionario.
* values(): Devuelve una lista de valores.

'''
# Eliminar todos los elementos de un diccionario
diccionario = {"nombre": "Juan", "edad": 20}
diccionario.clear()
print(diccionario)
# {}

# Devolver una copia de un diccionario
diccionario = {"nombre": "Juan", "edad": 20}
copia = diccionario.copy()
print(copia)
# {"nombre": "Juan", "edad": 20}

# Devolver el valor asociado a una clave
diccionario = {"nombre": "Juan", "edad": 20}
valor = diccionario.get("nombre")
print(valor)
# Juan

# Devolver una lista de pares (clave, valor)
diccionario = {"nombre": "Juan", "edad": 20}
pares = diccionario.items()
print(pares)
# [("nombre", "Juan"), ("edad", 20)]

# Devolver una lista de claves
diccionario = {"nombre": "Juan", "edad": 20}
claves = diccionario.keys()
print(claves)
# ["nombre", "edad"]

# Eliminar el elemento asociado a una clave
diccionario = {"nombre": "Juan", "edad": 20}
valor = diccionario.pop("nombre")
print(valor)
# Juan
print(diccionario)
# {"edad": 20}

# Agregar o actualizar los elementos de un diccionario
diccionario = {"nombre": "Juan", "edad": 20}
diccionario.update({"pais": "Argentina"})
print(diccionario)
# {"nombre": "Juan", "edad": 20, "pais": "Argentina"}

# Devolver una lista de valores
diccionario = {"nombre": "Juan", "edad": 20}
valores = diccionario.values()
print(valores)
# [Juan, 20]
'''
## Ejercicios
1. Crea un diccionario que contenga la información de una persona, como su nombre, edad, dirección y teléfono. Luego, utiliza los métodos get(), update() y pop() para modificar la información del diccionario.

# Crear un diccionario con información de una persona
persona = {
    "nombre": "Juan",
    "edad": 30,
    "direccion": "123 Calle Principal",
    "telefono": "555-123-4567"
}

# Utilizar el método get() para obtener el valor de una clave
print("Nombre:", persona.get("nombre"))
print("Edad:", persona.get("edad"))
print("Teléfono:", persona.get("telefono"))

# Utilizar el método update() para modificar el diccionario
nueva_informacion = {
    "edad": 31,
    "direccion": "456 Nueva Dirección",
    "email": "juan@example.com"
}
persona.update(nueva_informacion)

print("\nInformación actualizada:")
print("Nombre:", persona["nombre"])
print("Edad:", persona["edad"])
print("Dirección:", persona["direccion"])
print("Teléfono:", persona["telefono"])
print("Email:", persona.get("email"))  # La nueva clave "email"

# Utilizar el método pop() para eliminar una entrada del diccionario
clave_a_eliminar = "telefono"
if clave_a_eliminar in persona:
    persona.pop(clave_a_eliminar)

print("\nInformación después de eliminar el teléfono:")
print("Nombre:", persona["nombre"])
print("Edad:", persona["edad"])
print("Dirección:", persona["direccion"])
print("Teléfono:", persona.get("telefono", "No disponible"))  # El teléfono ya no está en el diccionario


2. Crea un diccionario que contenga el precio de una lista de productos. Luego, utiliza los métodos keys(), values() e items() para recorrer el diccionario y mostrar la información de cada producto.

# Crear un diccionario con los precios de los productos
precios_productos = {
    "manzanas": 1.0,
    "plátanos": 0.5,
    "naranjas": 0.75,
    "uvas": 2.0,
    "peras": 1.25
}

# Utilizar el método keys() para recorrer las claves (nombres de los productos)
print("Productos disponibles:")
for producto in precios_productos.keys():
    print(producto)

# Utilizar el método values() para recorrer los valores (precios de los productos)
print("\nPrecios de los productos:")
for precio in precios_productos.values():
    print("$", precio)

# Utilizar el método items() para recorrer las claves y valores juntos
print("\nInformación detallada:")
for producto, precio in precios_productos.items():
    print(f"Producto: {producto}, Precio: ${precio}")


3. Crea un diccionario que contenga la temperatura de una lista de ciudades. Luego calcule la media,max y minima de las temperaturas.

# Crear un diccionario con las temperaturas de las ciudades
temperaturas = {
    "Nueva York": 75,
    "Los Ángeles": 85,
    "Chicago": 68,
    "Houston": 92,
    "Miami": 88
}

# Calcular la temperatura media
temperatura_media = sum(temperaturas.values()) / len(temperaturas)

# Calcular la temperatura máxima
temperatura_maxima = max(temperaturas.values())

# Calcular la temperatura mínima
temperatura_minima = min(temperaturas.values())

# Mostrar los resultados
print("Temperatura media:", temperatura_media)
print("Temperatura máxima:", temperatura_maxima)
print("Temperatura mínima:", temperatura_minima)


4. Crea un diccionario que contenga el nombre de un país y su capital. Luego, utiliza el método update() para agregar un nuevo elemento al diccionario.

# Crear un diccionario con países y sus capitales
paises_capitales = {
    "Francia": "París",
    "Alemania": "Berlín",
    "España": "Madrid",
    "Italia": "Roma",
    "Reino Unido": "Londres"
}

# Utilizar el método update() para agregar un nuevo país y su capital
nuevo_pais = {"Japón": "Tokio"}
paises_capitales.update(nuevo_pais)

# Mostrar el diccionario actualizado
print("Diccionario actualizado:")
for pais, capital in paises_capitales.items():
    print(f"{pais}: {capital}")


5. Crea una lista que contenga una lista de números. Luego, utiliza el método count() para contar el número de veces que aparece un elemento en la lista.

# Crear una lista de números
numeros = [1, 2, 3, 2, 4, 2, 5, 2, 6]

# Utilizar el método count() para contar cuántas veces aparece el número 2 en la lista
conteo = numeros.count(2)

# Mostrar el resultado
print(f"El número 2 aparece {conteo} veces en la lista.")


6. Crea una lista que contenga una lista de números. Luego, utiliza el método index() para obtener el índice de un elemento en la lista.

# Crear una lista de números
numeros = [10, 20, 30, 40, 50]

# Utilizar el método index() para obtener el índice del número 30 en la lista
indice = numeros.index(30)

# Mostrar el resultado
print(f"El número 30 se encuentra en el índice {indice} de la lista.")


## Algoritmo de ordenamiento
Buscar información
'''