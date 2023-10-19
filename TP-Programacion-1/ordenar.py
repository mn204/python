def ordenamiento_insercion(arreglo, orden):
    print("Ordenamiento por inserción " + orden)
    for i in range(len(arreglo)):
        valor = arreglo[i]
        j = i - 1
        if orden == "ASC":
            while j >= 0 and arreglo[j] > valor:
                arreglo[j + 1] = arreglo[j]
                j -= 1
        elif orden == "DESC":
            while j >= 0 and arreglo[j] < valor:
                arreglo[j + 1] = arreglo[j]
                j -= 1
        arreglo[j + 1] = valor

    for elemento in arreglo:
        print(elemento, end=" ")
    print()

def ordenamiento_burbuja(arreglo, orden):
    print("Algoritmo de la burbuja " + orden)
    n = len(arreglo)
    intercambiado = True
    while intercambiado:
        intercambiado = False
        for i in range(1, n):
            if (orden == "ASC" and arreglo[i - 1] > arreglo[i]) or (orden == "DESC" and arreglo[i - 1] < arreglo[i]):
                arreglo[i - 1], arreglo[i] = arreglo[i], arreglo[i - 1]
                intercambiado = True

    for elemento in arreglo:
        print(elemento, end=" ")
    print()

def ordenamiento_seleccion(arreglo, orden):
    print("Ordenamiento por selección " + orden)
    n = len(arreglo)
    for i in range(n - 1):
        minimo = i
        for j in range(i + 1, n):
            if (orden == "ASC" and arreglo[j] < arreglo[minimo]) or (orden == "DESC" and arreglo[j] > arreglo[minimo]):
                minimo = j
        arreglo[i], arreglo[minimo] = arreglo[minimo], arreglo[i]

    for elemento in arreglo:
        print(elemento, end=" ")
    print()

# Ejemplo de uso
arreglo = [5, 2, 9, 1, 5, 6, 3]
orden = "ASC"  # Puedes cambiar a "DESC" para ordenamiento descendente

ordenamiento_insercion(arreglo.copy(), orden)
ordenamiento_burbuja(arreglo.copy(), orden)
ordenamiento_seleccion(arreglo.copy(), orden)