#ALUMNO: LEPKA AGUSTIN MARIO NICOLAS
#COMISION: M2025-25

#Trabajo practico 4: estructuras repetitivas

#Actividad 1

#Se inicializa un bucle for para que en cada iteracion se imprima en pantalla los nros del 0 al 100.
for inicio in range(101):
    print(inicio)

#Actividad 2

#Se solicita al usuario que ingrese un numero entero para calcular su cantidad de digitos que contiene
numero = int(input("Ingresa un numero entero:"))

#Se declara una variable como contador
contador = 0
#Se usa un while para contar la cantidad de veces que el numero ingresado puede ser dividido por 10 en una division entera
while numero > 0:
    contador = contador + 1
    numero = numero // 10
#Se imprime el contador que acumula la cantidad de digitos.
print(contador)

#Actividad 3

#Se pide al usuario que ingrese dos numeros para calcular la suma de todos los numeros que haya dentro del rango indicado sin sumar los extremos
num1, num2 = int(input("Ingresa el primer numero:")), int(input("Ingresa segundo numero:"))

contador = 0

for num in range(num1 + 1, num2):
    contador = contador + num

print(contador)

#Actividad 4

#Se inicia un acumulador en 0 para que guarde la suma de los numeros

acumulador1 = 0

#Se inicia un bucle while el cual siempre ejecutara ya que su condicion es siempre verdadera, se detendra cuando alcance la condicion 
# de la bandera.

while True:
    #Se pide al usuario que ingrese un numero entero

    numero_ingresado = int(input("Ingrese un numero entero:"))
    
    #Se inicia el condicional if para que funcione como bandera y el ciclo logre detenerse
    if(numero_ingresado == 0):
        break
    
    #El acumulador empieza a guardar el primer numero y a partir de la segunda iteracion en caso de ser posible suma el siguiente numero ingresado por el usuario
    
    acumulador1 = acumulador1 + numero_ingresado
    print(f"la suma total de los nros ingresados es {acumulador1}")

#Actividad 5

import random

incognita = random.randint(1, 8)

intento = int(input("Ingrese un numero entero entre el 0 y 9 para intentar adivinar el numero incognita:"))

while  intento != incognita:
    
    siguiente_intento = int(input("Ingrese otro numero para intentar adivinar:"))

#Actividad 6

#Imprime todos los números pares entre 0 y 100 en orden decreciente
for num in range(100, -1, -1):  #desde 100 hasta 0, en pasos de -1
    if num % 2 == 0:
        print(num)

#Actividad 7

#Solicita al usuario un número entero positivo
n = int(input("Ingresá un número entero positivo: "))

#Verificamos que sea positivo
if n >= 0:
    suma = 0
    for i in range(n + 1):  #desde 0 hasta n inclusive
        suma += i
    print("La suma de los números entre 0 y", n, "es:", suma)
else:
    print("El número ingresado no es positivo.")

#Actividad 8

#Cantidad de números a ingresar (podés cambiar este valor para pruebas)
CANTIDAD_NUMEROS = 100

#Inicializamos los contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

print("Ingresá", CANTIDAD_NUMEROS, "números enteros:")

for i in range(CANTIDAD_NUMEROS):
    num = int(input(f"Número {i + 1}: "))
    
    #Verificamos si es par o impar
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    #Verificamos si es positivo o negativo (el 0 no se cuenta como ninguno)
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

#Mostramos los resultados
print("\nResultados:\nCantidad de números pares:, pares,\nCantidad de números impares:, impares\nCantidad de números positivos:, positivos\nCantidad de números negativos:, negativos")

#Actividad 9

#Cantidad de números a ingresar (podés ajustar este valor para pruebas)
CANTIDAD_NUMEROS = 100

suma = 0  #Acumulador para la suma total

print("Ingresá", CANTIDAD_NUMEROS, "números enteros para calcular su media:")

for i in range(CANTIDAD_NUMEROS):
    num = int(input(f"Número {i + 1}: "))
    suma += num  #Acumulamos los números

#Calculamos la media
media = suma / CANTIDAD_NUMEROS
print("\nLa media de los números ingresados es:", media)

#Actividad 10

#Pedimos al usuario que ingrese un número
numero = input("Ingresá un número para invertir sus dígitos: ")

#Usamos slicing para invertir el string
numero_invertido = numero[::-1]

print("El número invertido es:", numero_invertido)
