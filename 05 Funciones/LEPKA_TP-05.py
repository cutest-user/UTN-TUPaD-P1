#Alumno: LEPKA AGUSTIN MARIO NICOLAS
#Comision: 25

#Actividad 1: Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”

def imprimir_hola_mundo():
    print("Hola Mundo!")

#Actividad 2: Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:“Hola Marcos!”
def saludar_usuario(nombre):
    #Devuelve un saludo personalizado con el nombre recibido
    return f"Hola {nombre}!"

#Actividad 3: Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#Actividad 4: Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_ circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo
def calcular_area_circulo(radio):
    import math
    #Área = π * radio^2
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    import math
    #Perímetro = 2 * π * radio
    return 2 * math.pi * radio

#Actividad 5: Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes.
def segundos_a_horas(segundos):
    #1 hora = 3600 segundos
    return segundos / 3600

#Actividad 6: Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10.
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

#Actividad 7: Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos.
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    #Para evitar división por cero, se controla
    if b != 0:
        division = a / b
    else:
        division = None  #O podría devolver un mensaje de error
    return (suma, resta, multiplicacion, division)

#Actividad 8: Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC)
def calcular_imc(peso, altura):
    #IMC = peso / (altura^2)
    return peso / (altura ** 2)

#Actividad 9: Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit.
def celsius_a_fahrenheit(celsius):
    #F = C * 9/5 + 32
    return celsius * 9 / 5 + 32

#Actividad 10: Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

#Programa main que llama a todas las funciones

if __name__ == "__main__":
    
    #Actividad 1
    imprimir_hola_mundo()
    print()

    #Actividad 2
    nombre_del_usuario = input("Ingrese su nombre: ")
    saludo = saludar_usuario(nombre_del_usuario)
    print(saludo)
    print()

    #Actividad 3
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    residencia = input("Ingrese su residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)
    print()

    #Actividad 4
    radio = float(input("Ingresa el radio del círculo: "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"Área del círculo: {area:.2f}")
    print(f"Perímetro del círculo: {perimetro:.2f}")
    print()

    #Actividad 5
    segundos = int(input("Ingresa la cantidad de segundos: "))
    horas = segundos_a_horas(segundos)
    print(f"{segundos} segundos equivalen a {horas:.2f} horas")
    print()

    #Actividad 6
    num = int(input("Ingrese un número para la tabla de multiplicar: "))
    tabla_multiplicar(num)
    print()

    #Actividad 7
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    resultados = operaciones_basicas(a, b)
    print(f"Suma: {resultados[0]}")
    print(f"Resta: {resultados[1]}")
    print(f"Multiplicación: {resultados[2]}")
    if resultados[3] is not None:
        print(f"División: {resultados[3]}")
    else:
        print("División: Error - División por cero no permitida")
    print()

    #Actividad 8
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")
    print()

    #Actividad 9
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")
    print()

    #Actividad 10
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    promedio = calcular_promedio(num1, num2, num3)
    print(f"El promedio de los números es: {promedio:.2f}")
