#ALUMNO: Lepka, Agustin
#COMISION: M2025-25

#Trabajo practico 03: Estructuras condicionales

# -Actividad 1

#Se pide al usuario que ingrese el numero que representa su edad
edad_ingresada = int(input("Ingrese su edad: "))
#Si se cumple la primera condicion su bloque indicara que es mayor de edad
if edad_ingresada >= 18:
    print("Usted es mayor de edad.")
#Si no se cumple la condicion anterior el ultimo bloque del condicional indicara que es menor de edad.
else:
    print("Usted es menor de edad.")

# -Actividad 2

#Se pide al usuario que ingrese el numero que representa su nota
nota_ingresada = int(input("Ingrese su nota: "))
#Si se cumple la primera condicion su bloque indicara que esta aprobado
if nota_ingresada >= 6:
    print("Usted esta aprobado.")
#Si no se cumple la condicion anterior el ultimo bloque del condicional indicara que esta desaprobado.
else:
    print("Usted esta desaprobado")

# -Actividad 3

#Se pide al usuario que ingrese un numero para verificar si es par o impar.
numero_clasificado = int(input("Ingrese un numero para saber si es par o impar: "))
#En la primer condicion se verifica si el numero ingresado tiene como resto 0 en modulo 2, si el resto es 0 es par.
if numero_clasificado % 2 == 0:
    print("El numero ingresado es par.")
#En la condicion final si no se cumple la condicion anterior imprime que el numero es impar
else:
    print("El numero ingresado es impar.")

# -Actividad 4

#Se pide al usuario que ingrese su edad
clasificar_edad = int(input("Ingrese su edad para saber a que grupo pertenece: "))

#En la primera condicion se indica que el usuario es un niño si su edad es menor a 12.
if clasificar_edad < 12:
    print("Usted es un niño.")
#En la segunda condicion se indica que el usuario es un adolescente si su edad es mayor o igual a 12 y menor que 18.
elif (clasificar_edad >= 12) and (clasificar_edad < 18):
    print("Usted es un adolescente.")
#En la tercera condicion se indica que el usuario es un adulto joven si su edad es mayor o igual que 18 y menor que 30.
elif (clasificar_edad >= 18) and (clasificar_edad < 30):
    print("Usted es un adulto joven.")
#En la cuarta condicion se indica que el usuario es un adulto si su edad es mayor o igual a 30.
elif (clasificar_edad >= 30):
    print("Usted es un adulto.")

#Actividad 5

#Se pide al usuario que ingrese una contraseña que tenga entre como minimo 8 y como maximo 14 caracteres

contraseña = str(input("Ingrese una contraseña con un minimo de 8 y maximo 14 caracteres: "))

#Se almacena la cantidad de caracteres ingresados en una variable

longitud_contraseña = len(contraseña)

#Se usa una estructura condicional para mostrar en pantalla si la contraseña ingresada es correcta o no
if longitud_contraseña >= 8 and longitud_contraseña <=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Actividad 6

#Se importan los modulos necesarios
import statistics, random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

#Se almacena en variables los valores de moda, media y mediana

moda = statistics.mode(numeros_aleatorios)
media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)

#Se muestran los resultados de moda, media y mediana por pantalla

print(f"{moda}\n{media}\n{mediana}")

#Con una estructura condicional se decide que tipo de sesgo tiene el resultado de la lista de numeros aleatorios

if media > mediana and mediana > moda:
    print("El sesgo es positivo.")
elif media < mediana and mediana < moda:
    print("El sesgo es negativo.")
elif media == mediana == moda:
    print("Sin sesgo.")
else:
    print("No se puede determinar el sesgo.")

#Actividad 7

#Se pide al usuario que ingrese una palabra
palabra = str(input("Ingresa una palabra:"))

#Se extrae el ultimo caracter de la palabra ingresada
ultima_letra = palabra[-1]

#Se almacenan las vocales en una variable
vocales = "aeiou"
#Mediante estructura condicional se imprime la palabra con un signo de exclamacion al final si termina con vocal, de lo contrario se imprime tal como fue ingresado
if ultima_letra.lower() in vocales:
    print(palabra + "!")
else:
    print(palabra)

#Actividad 8

#Se pide al usuario que ingrese su nombre
nombre = str(input("Ingrese su nombre:"))
#Se pide al usuario que ingrese una opcion
opcion = int(input("Ingrese una opcion:\nOpcion 1: su nombre se escribira solo en mayusculas\nOpcion 2: su nombre se escribira solo en minusculas\nOpcion 3: su nombre tendra en mayuscula solo la primera letra\n"))
#Con una estructura condicional se procede segun la opcion elegida
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())

#Actividad 9

#Se pide al usuario que ingrese la magnitud de un terremoto
magnitud = float(input("Ingrese la magnitud de un terremoto:"))
#Se clasifica la magnitud ingresada con la estructura condicional
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala). ")

#Actividad 10

#Solicitar al usuario la información necesaria
hemisferio = input("¿En qué hemisferio te encontrás? (N/S): ").upper()
mes = input("¿Qué mes es? (ej: marzo): ").lower()
dia = int(input("¿Qué día del mes es? (número): "))

#Diccionario para convertir meses a números
meses = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4,
    "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
    "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
}

#Verificar si el mes ingresado es válido
if mes not in meses:
    print("Mes inválido.")
else:
    numero_mes = meses[mes]

    #Convertir fecha a formato MMDD
    fecha = numero_mes * 100 + dia

    # Estaciones por rangos MMDD (formato mesdía)
    if hemisferio == "N":
        if 1221 <= fecha <= 320:
            estacion = "invierno"
        elif 321 <= fecha <= 620:
            estacion = "primavera"
        elif 621 <= fecha <= 920:
            estacion = "verano"
        elif 921 <= fecha <= 1220:
            estacion = "otoño"
        else:  # Para fechas como enero (por ejemplo, 0110)
            estacion = "invierno"
    elif hemisferio == "S":
        if 1221 <= fecha <= 320:
            estacion = "verano"
        elif 321 <= fecha <= 620:
            estacion = "otoño"
        elif 621 <= fecha <= 920:
            estacion = "invierno"
        elif 921 <= fecha <= 1220:
            estacion = "primavera"
        else:
            estacion = "verano"
    else:
        estacion = None
        print("Hemisferio no válido. Usá N o S.")

    # Mostrar resultado si se obtuvo una estación
    if estacion:
        print(f"La estación del año es: {estacion.capitalize()}")