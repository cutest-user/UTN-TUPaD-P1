# Actividad 1
# Se solicita al usuario que ingrese su nombre
nombre = input("Ingresa tu nombre: ")
# Luego se imprime un saludo con el nombre ingresado
print(f"Hola {nombre}")

# Actividad 2
# Se solicita al usuario que ingrese su nombre, apellido, edad y lugar de residencia

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")
# Luego se imprime una frase con estos datos
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Actividad 3
# Se solicita al usuario que ingrese su nombre, apellido, edad y lugar de residencia

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar_residencia = input("Ingrese su lugar de residencia: ")
# Luego se imprime una frase con estos datos de forma similar a la actividad 2
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}.")

# Actividad 4
# Se pide al usuario el radio de un círculo y se importa la liberia math para poder usar pi.
import math
radio = float(input("Ingrese el radio del circulo: "))
# Luego se calcula el área y el perímetro del círculo usando fórmulas matemáticas
area = math.pi * radio ** 2  # Fórmula para el área de un círculo
perimetro = 2 * math.pi * radio  # Fórmula para el perímetro de un círculo
# Finalmente se imprime los resultados con 3 decimales
print(f"El area del circulo es: {area:.3f}")
print(f"El perimetro del circulo es: {perimetro:.3f}")

# Actividad 5
# Se solicita al usuario una cantidad de segundos

segundos = int(input("Ingrese una cantidad de segundos: "))
# Se convierte esa cantidad de segundos a horas 
horas = segundos / 3600  # Conversión de segundos a horas
# Se muestra el resultado con 2 decimales
print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

# Actividad 6
# Se solicita al usuario un número
numero = int(input("Ingrese un número: "))
# Se imprime la tabla de multiplicar de ese número del 1 al 10
print(f"Tabla de multiplicar del {numero}:")
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

# Actividad 7
# Se solicitan dos números
num1 = int(input("Ingrese el primer número (distinto de 0): "))
num2 = int(input("Ingrese el segundo número (distinto de 0): "))
# Se realizan las operaciones de suma, resta, multiplicación y división
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
# Luego se imprime el resultado de cada operación
print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Multiplicación: {num1} x {num2} = {multiplicacion}")
print(f"División: {num1} / {num2} = {division}")

# Actividad 8
# Se solicita al usuario su altura y peso

altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
# Luego se calcula el índice de masa corporal (IMC) usando la fórmula IMC = peso / altura^2
indiceMasaCorporal = peso / altura ** 2
# Se imprime el IMC
print(f"Su indice de masa corporal es: {indiceMasaCorporal}")

# Actividad 9
# Se solicita al usuario una temperatura en grados Celsius

tempCelsius = int(input("Ingrese el primer número (distinto de 0): "))
# Luego se convierte esa temperatura a grados Fahrenheit usando la fórmula: F = (C * 9/5) + 32
conversionAFarenheit = 9/5 * tempCelsius + 32
# Se imprime la conversion
print(f"La temp Celsius ingresada equivale a: {conversionAFarenheit} Farenheit")

# Actividad 10
# Se solicitan tres números
num1 = float(input("Ingrese el primer número"))
num2 = float(input("Ingrese el segundo número"))
num3 = float(input("Ingrese el tercer número"))
# Se calcula el promedio de esos tres números
promedio = (num1 + num2 + num3) / 3  # Cálculo del promedio de los tres números
# Se imprime el promedio
print(f"El promedio de los 3 numeros es: {promedio}")
