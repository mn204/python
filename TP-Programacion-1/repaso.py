'''
Ejercicio 1: Calculadora simple Crea una calculadora que acepte dos números y
un operador (+, -, *, /) como entrada del usuario y devuelva el resultado de la
operación.
def calcular(num1, num2, operador):
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: División por cero"
    else:
        return "Operador no válido"

# Solicitar entrada del usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operador = input("Ingrese el operador (+, -, *, /): ")

# Calcular y mostrar el resultado
resultado = calcular(num1, num2, operador)
print(f"Resultado: {resultado}")

Ejercicio 2: Validación de contraseña Escribe un programa que solicite al usuario
ingresar una contraseña y luego la valide según ciertos criterios (por ejemplo,
debe tener al menos 8 caracteres, incluyendo letras mayúsculas, minúsculas y
números).

# Función para validar una contraseña
def validar_contrasena(contrasena):
    if len(contrasena) < 8:
        return False
    tiene_minusculas = False
    tiene_mayusculas = False
    tiene_numeros = False
    for caracter in contrasena:
        if caracter.islower():
            tiene_minusculas = True
        if caracter.isupper():
            tiene_mayusculas = True
        if caracter.isdigit():
            tiene_numeros = True
    return tiene_minusculas and tiene_mayusculas and tiene_numeros

# Solicitar una contraseña al usuario
contrasena = input("Ingrese una contraseña: ")

# Validar la contraseña
if validar_contrasena(contrasena):
    print("Contraseña válida.")
else:
    print("Contraseña no válida. Asegúrese de que tenga al menos 8 caracteres, incluyendo letras mayúsculas, minúsculas y números.")


Ejercicio 3: Contador de palabras Escribe un programa que cuente la cantidad
de palabras en una cadena de texto. Puedes suponer que las palabras están
separadas por espacios.

def contar_palabras(cadena):
    palabras = cadena.split()  # Dividir la cadena en palabras por espacios en blanco
    return len(palabras)

# Solicitar una cadena de texto al usuario
texto = input("Ingrese una cadena de texto: ")

# Contar palabras y mostrar el resultado
cantidad_palabras = contar_palabras(texto)
print(f"La cadena de texto tiene {cantidad_palabras} palabras.")

Ejercicio 4: Números primos Escribe un programa que solicite al usuario ingresar
un número y determine si es un número primo o no.

def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

# Solicitar un número al usuario
numero = int(input("Ingrese un número: "))

# Determinar si el número es primo y mostrar el resultado
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")


Ejercicio 5: Juego de adivinanza Crea un juego en el que el programa elija
un número aleatorio y el usuario tenga que adivinarlo. El programa debe proporcionar pistas para indicar si el número a adivinar es mayor o menor que el
número ingresado por el usuario. El juego debe continuar hasta que el usuario
adivine correctamente.

import random

# Generar un número aleatorio entre 1 y 100
numero_a_adivinar = random.randint(1, 100)

intentos = 0
adivinado = False

print("Bienvenido al juego de adivinanza. Adivina el número entre 1 y 100.")

while not adivinado:
    intento = int(input("Ingresa tu suposición: "))
    intentos += 1

    if intento == numero_a_adivinar:
        adivinado = True
    elif intento < numero_a_adivinar:
        print("El número a adivinar es mayor.")
    else:
        print("El número a adivinar es menor.")

print(f"Felicidades, adivinaste el número {numero_a_adivinar} en {intentos} intentos.")


Ejercicio 6: Generador de secuencias Fibonacci Escribe un programa que genere
los primeros n términos de la secuencia Fibonacci, donde n es un número ingresado por el usuario.

def generar_fibonacci(n):
    secuencia = []
    a, b = 0, 1
    for _ in range(n):
        secuencia.append(a)
        a, b = b, a + b
    return secuencia

# Solicitar al usuario la cantidad de términos de la secuencia Fibonacci
n = int(input("Ingrese la cantidad de términos de la secuencia Fibonacci que desea generar: "))

# Generar y mostrar los términos de la secuencia Fibonacci
secuencia_fibonacci = generar_fibonacci(n)
print(f"Los primeros {n} términos de la secuencia Fibonacci son:")
print(secuencia_fibonacci)



Ejercicio 8: Generador de números primos Escribe un programa que genere los
primeros n números primos, donde n es un número ingresado por el usuario.

def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def generar_primos(n):
    primos = []
    numero = 2
    while len(primos) < n:
        if es_primo(numero):
            primos.append(numero)
        numero += 1
    return primos

# Solicitar al usuario la cantidad de números primos que desea generar
n = int(input("Ingrese la cantidad de números primos que desea generar: "))

# Generar y mostrar los primeros n números primos
numeros_primos = generar_primos(n)
print(f"Los primeros {n} números primos son:")
print(numeros_primos)


Ejercicio 9: Conversión de números romanos Crea un programa que permita al
usuario ingresar un número romano y lo convierta a su equivalente en números
arábigos.

def romano_a_arabigo(numero_romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    arabigo = 0
    anterior_valor = 0

    for caracter in numero_romano[::-1]:
        valor = valores[caracter]

        if valor < anterior_valor:
            arabigo -= valor
        else:
            arabigo += valor

        anterior_valor = valor

    return arabigo

# Solicitar al usuario un número romano
numero_romano = input("Ingrese un número romano: ")

# Convertir el número romano a arábigo y mostrar el resultado
try:
    numero_arabigo = romano_a_arabigo(numero_romano)
    print(f"El número romano {numero_romano} es igual a {numero_arabigo} en números arábigos.")
except KeyError:
    print("Entrada no válida. Asegúrese de que el número romano sea válido.")

Ejercicio 10: Validación de paréntesis Escribe un programa que verifique si
una cadena de texto contiene paréntesis balanceados. Por ejemplo, “(())” es
balanceado, pero “(()))” no lo es.

def paréntesis_balanceados(cadena):
    pila = []
    for carácter in cadena:
        if carácter == '(':
            pila.append(carácter)
        elif carácter == ')':
            if not pila:
                return False  # Hay un cierre sin apertura correspondiente
            pila.pop()
    
    return not pila  # La pila debe estar vacía para que los paréntesis estén balanceados

# Solicitar una cadena de texto al usuario
cadena = input("Ingrese una cadena de texto con paréntesis: ")

# Verificar si los paréntesis están balanceados y mostrar el resultado
if paréntesis_balanceados(cadena):
    print("Los paréntesis están balanceados.")
else:
    print("Los paréntesis no están balanceados.")

# Inicializamos una lista vacía para almacenar los usuarios
usuarios = []

while True:
    usuario = input("Ingrese un nombre de usuario (o 'salir' para salir): ")
    
    if usuario.lower() == 'salir':
        break  # Si el usuario ingresa 'salir', salimos del programa
    
    # Verificamos si el usuario ya existe en la lista
    if usuario in usuarios:
        print("El usuario ya existe. Por favor, elija otro nombre de usuario.")
        continue
    
    contrasena = input("Ingrese una contraseña: ")
    
    # Verificamos si la contraseña cumple con los requisitos
    if (any(c.isupper() for c in contrasena) and
        any(c.islower() for c in contrasena) and
        any(c.isalnum() or not c.isalpha() for c in contrasena) and
        len(contrasena) >= 12):
        print("Usuario y contraseña creados exitosamente.")
        usuarios.append(usuario)
    else:
        print("La contraseña no cumple con los requisitos. Debe tener al menos 12 caracteres, una mayúscula, una minúscula y un símbolo especial.")

'''

