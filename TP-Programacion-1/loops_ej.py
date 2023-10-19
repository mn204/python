'''
Ejercicios de bucles
1. Imprime los números del 1 al 100, pero solo los números pares.

for i in range (1,101,1):
    if i%2==0:
        print(i)


2. Imprime los números del 1 al 100, pero solo los números divisibles por 3.

for i in range (1,100,1):
    if i%3 == 0:
        print(i)

3. Imprime los números del 1 al 100, pero solo los números primos.

for i in range (2,101):
    primo = True
    for j in range(2,i):
        if i % j == 0:
            primo = False
            break
    if primo:
        print(i)

4. Imprime una pirámide de números.

altura = 5
for i in range(1, altura + 1):
    
    for j in range(altura - i):
        print(" ", end=" ")
    
    for k in range(1, i + 1):
        print(k, end=" ")

    for l in range(i - 1, 0, -1):
        print(l, end=" ")

    print()


5. Imprime un menú de opciones y permita al usuario seleccionar una opción.
6. Escribir un programa que pida al usuario un número entero y muestre por
pantalla un triángulo rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1

altura = int(input("Ingresa un n de altura de piramide: "))
for i in range(1, altura + 1):
    for j in range(2 * i - 1, 0, -2):
        print(j, end=" ")
    print()

7. Escribir un programa que almacene la cadena de caracteres contraseña en
una variable, pregunte al usuario por la contraseña hasta que introduzca la
contraseña correcta. Números primos: Escribe un programa que encuentre
y muestre los primeros 100 números primos.

contrasenia = "lasagna"
while True :
    cadena  = input("ingrese una contrasenia: ")
    if cadena == contrasenia:
        print("contrasenia correcta")
        break
    else:
        print("Contrasenia incorrecta")

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

n_primos = 0
numero = 2

while n_primos < 100:
    if es_primo(numero):
        print(numero, end=" ")
        n_primos += 1
    numero += 1


8. Secuencia de Fibonacci personalizada: Escribe un programa que genere
una secuencia de Fibonacci de n términos, donde n es ingresado por el
usuario. Además, verifica si cada número en la secuencia es primo o no y
almacena los primos en una lista


def fibonacci(num):
    if num == 1 or num == 0:
        return num
    else:
        return fibonacci(num-2) + fibonacci(num-1)
    
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

n = int(input("Ingrese hasta que nro mostrar de fibonacci: "))
fibonPrimos= []
for i in range (n):
    print(fibonacci(i))
    if es_primo(fibonacci(i)):
        fibonPrimos.append(fibonacci(i))
print("Los numeros primos de la secuencia de fibonacci son:")
print(fibonPrimos)

9. Matriz espiral: Dada una matriz cuadrada de tamaño n, escribe un programa que imprima la matriz en forma de espiral. Por ejemplo, para n =
4, la salida debería ser:
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7


def matriz_espiral(n):
    matriz = [[0] * n for _ in range(n)]

    valor = 1
    fila_inicio, fila_fin, columna_inicio, columna_fin = 0, n - 1, 0, n - 1

    while fila_inicio <= fila_fin and columna_inicio <= columna_fin:
        for i in range(columna_inicio, columna_fin + 1):
            matriz[fila_inicio][i] = valor
            valor += 1
        fila_inicio += 1

        for i in range(fila_inicio, fila_fin + 1):
            matriz[i][columna_fin] = valor
            valor += 1
        columna_fin -= 1

        if fila_inicio <= fila_fin:
            for i in range(columna_fin, columna_inicio - 1, -1):
                matriz[fila_fin][i] = valor
                valor += 1
            fila_fin -= 1

        if columna_inicio <= columna_fin:
            for i in range(fila_fin, fila_inicio - 1, -1):
                matriz[i][columna_inicio] = valor
                valor += 1
            columna_inicio += 1

    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()


n = 4
matriz_espiral(n)

10. Adivina el número: Crea un programa en el que la computadora elija
un número aleatorio entre 1 y 100, y el usuario tiene que adivinarlo en la
menor cantidad de intentos posible. El programa debe proporcionar pistas
(“Demasiado alto” o “Demasiado bajo”) después de cada intento.

numero_secreto = int(input('numero secreto'))

def adivina_numero(numero_secreto):
    intentos = 0

    while True:
        intento = int(input("Adivina el número: "))
        intentos += 1

        if intento < numero_secreto:
            print("Demasiado bajo.")
        elif intento > numero_secreto:
            print("Demasiado alto.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

adivina_numero(numero_secreto)


11. Juego de la vida de Conway: Implementa el “Juego de la vida” de Conway. Este es un simulador de autómatas celulares que evoluciona según
reglas simples. Puede ser un desafío implementar las reglas y mostrar la
evolución en una cuadrícula.
12. Cálculo de PI: Usa una serie infinita para calcular el valor de fi. Puedes
utilizar la serie de Leibniz o la serie de Nilakantha.
13. Ordenamiento personalizado: Escribe un programa de ordenamiento que
ordene una lista de números en función de un criterio personalizado. Por
ejemplo, puedes ordenar los números por la suma de sus dígitos en orden
ascendente.

def ordenamiento_burbuja(lista, criterio="asc"):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (criterio == "asc" and lista[j] > lista[j + 1]) or (criterio == "desc" and lista[j] < lista[j + 1]):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


numeros = [5, 2, 9, 1, 5, 6, 3]

criterio = input("Ingrese 'asc' para ordenar de forma ascendente o 'desc' para ordenar de forma descendente: ")

ordenamiento_burbuja(numeros, criterio)

print("Lista ordenada:", numeros)

14. Calculadora de expresiones matemáticas: Desarrolla una calculadora que
pueda evaluar expresiones matemáticas complejas, como aquellas que incluyen paréntesis y operadores como +, -, *, /, ^ (exponente).

'''




