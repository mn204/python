'''1. Número positivo o negativo: Escribe un programa que tome un número como entrada y muestre un mensaje
indicando si es positivo, negativo o igual a cero.

print('1. ingrese n')
n1= int(input())
if n1>0:
    print('positivo')
elif n1<0:
    print('negativo')
else :
   print( 'es 0' )

2. Calculadora simple: Crea una calculadora que permita al usuario ingresar dos números y una operación (suma,
resta, multiplicación o división) y luego muestre el resultado.

print('2. ingresw n1 y n2')
n1= int(input ())
n2= int(input ())
print('ingrese operacion: suma, mult, resta, division')
operador= input()
if operador == 'suma':
    print(n1+n2)
elif operador == 'resta':
    print(n1-n2)
elif  operador == 'division':
    print (n1/n2)
elif  operador == 'mult':
    print (n1*n2)
    

3. Edad y votación: Pide al usuario su edad y luego determina si es elegible para votar en las elecciones (mayor de
18 años) o si todavía es demasiado joven.

print('3. ingrese edad')
edad1 = int(input())
print( 'es mayor para votar' if edad1 >= 18 else 'es menor para votar' )

4. Mayor de tres números: Solicita al usuario ingresar tres números y muestra cuál es el número más grande de los
tres.

print('ingrese 3 numeros')
n1= int(input ())
n2= int(input ())
n3= int(input ())
if n1>n2 and n1>n3:
    print(n1, 'es mayor')
elif n2>n3:
    print (n2, 'es mayor')
else:
    print (n3, 'es mayor')
5. Días en un mes: Pide al usuario que ingrese un mes (como un número del 1 al 12) y muestra cuántos días tiene
ese mes. Considera los años bisiestos (febrero tiene 29 días).


print('ingrese n del 1 al 12')
n1= int(input ())
if n1 == 1 or (n1 < 8  and n1% 2== 1):
        print ('31 dias')
elif n1 != 2 and n1 < 7:
    print ('30 dias')
elif n1 != 2 and(n1>7  and n1 %2 == 0):
    print('31 dias')
elif n1 == 2:
    print ('febrero tiene 28 o 29 dias')
else:
    print('30 dias')




6. Categoría de edad: Pide al usuario su edad y clasifícalo en una de las siguientes categorías: niño (0-12 años),
adolescente (13-19 años), adulto (20-64 años) o adulto mayor (65 o más años).

print ('ingrese edad')
edad = int(input())
if edad >=0 and edad <13:
    print('ninio')
elif edad > 12 and edad < 20:
    print('adoles')
elif edad > 19 and edad <65:
    print('adulto')
elif edad > 64:
    print ('adulto mayor')

7. Calculadora de IMC: Crea una calculadora de Índice de Masa Corporal (IMC). Pide al usuario su peso en
kilogramos y su altura en metros, y luego calcula e informa su IMC, indicando si está bajo peso, peso normal,
sobrepeso u obesidad.

peso =int(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso/(altura**2)

if imc < 18:
    print("bajo peso")
elif imc > 17 and imc < 25:
    print("normal peso")
else:
    print("sobrepeso u obesidad")


8. Año bisiesto: Pide al usuario ingresar un año y verifica si es un año bisiesto o no. Un año es bisiesto si es
divisible por 4, pero no por 100, a menos que también sea divisible por 400.

anio = int(input("Ingrese año: "))
if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print("es bisiesto")
else:
    print("no es bisiesto")


9. Comparación de strings: Solicita al usuario que ingrese dos cadenas de texto y determina si son iguales o
diferentes. Además, verifica si una de las cadenas es un palíndromo (se lee igual al revés).

cad1 = input("ingrese cad 1: ")
cad2 = input("ingrese cad 2: ")

if cad1 == cad2:
    print("son iguales")
else:
    print ('no son iguales')

cad1_invertida = cad1[::-1]
cad2_invertida = cad2[::-1]
if cad1_invertida == cad1:
    print("La cadena 1 es palindroma.")
else:
    print("La cadena 1 no es palindroma. ")

if cad2_invertida == cad2:
    print("La cadena 2 es palindroma.")
else:
    print("La cadena 2 no es palindroma. ")


10. Aprobación de un examen: Pide al usuario que ingrese su calificación en un examen (0-100) y determina si ha
aprobado (calificación mayor o igual a 60) o ha reprobado.

examen = int(input("ingrese su calificación en un examen (0-100): "))
if examen >=60:
    print("aprobado")
else:
    print("desaprobado")

'''





