#Alumno: LEPKA AGUSTIN MARIO NICOLAS
#Comision: 25

#Práctico 6: Estructuras de datos complejas

#Ejercicio 1: Añadir frutas al diccionario
#Se crea un diccionario inicial con algunas frutas y sus precios
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

#Agregamos nuevas frutas con sus respectivos precios
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

#Ejercicio 2: Actualizar precios de algunas frutas
#Se modifica directamente el valor de ciertas claves del diccionario
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

#Ejercicio 3: Crear una lista con solo los nombres de las frutas
#Extraemos las claves del diccionario, que representan los nombres
nombres_frutas = list(precios_frutas.keys())

#Ejercicio 4: Agenda telefónica de 5 contactos
contactos = {}

#Se cargan 5 contactos con un bucle
for cargar in range(5):
    nombre = input("Ingresá el nombre del contacto: ")  #Se solicita el nombre del contacto
    telefono = input("Ingresá el número de teléfono: ")  #Se solicita el número de teléfono
    contactos[nombre] = telefono  #Se guarda la clave y el valor en el diccionario

#Se consulta un contacto a partir de su nombre
consulta = input("Ingresá el nombre del contacto a consultar: ")
if consulta in contactos:
    print(f"El número de {consulta} es {contactos[consulta]}")  #Mostramos el valor (número) si existe
else:
    print("Contacto no encontrado.")

#Ejercicio 5: Análisis de una frase ingresada por el usuario
frase = input("Ingresá una frase: ")  #Se pide una frase al usuario
palabras = frase.split()  #La frase se convierte en una lista de palabras

#Se crea un set para obtener las palabras únicas (sin repeticiones)
palabras_unicas = set(palabras)

#Se cuenta la frecuencia de cada palabra utilizando un diccionario
recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1  #Si ya existe, incrementamos el contador
    else:
        recuento[palabra] = 1  #Si no existe, lo inicializamos en 1

#Se imprimen los resultados
print(f"Palabras únicas: {palabras_unicas}")
print(f"Recuento: {recuento}")

#Ejercicio 6: Promedio de notas de 3 alumnos
alumnos = {}

#Se repite el proceso para 3 alumnos
for alumno in range(3):
    nombre = input("Ingresá el nombre del alumno: ")  #Solicita el nombre del alumno
    #Se usa una tupla para almacenar 3 notas enteras
    notas = tuple(int(input(f"Nota {posicion_notas+1} de {nombre}: ")) for posicion_notas in range(3))
    alumnos[nombre] = notas  #Guardamos las notas del alumno en el diccionario

#Se calcula y muestra el promedio de cada alumno
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)  #Promedio = suma de notas dividido por la cantidad
    print(f"Promedio de {nombre}: {promedio:.2f}")  # Mostramos con dos decimales

#Ejercicio 7: Operaciones con sets de estudiantes
#Se crean dos sets que representan los estudiantes que aprobaron cada parcial
parcial_1 = {"Ana", "Juan", "Pedro", "Sofia"}
parcial_2 = {"Juan", "Sofia", "Luis", "Maria"}

#Los estudiantes que aprobaron ambos parciales (conjuncion)
ambos = parcial_1 & parcial_2

#Los estudiantes que aprobaron solo uno de los dos (XOR)
solo_uno = parcial_1 ^ parcial_2

# Todos los estudiantes que aprobaron al menos un parcial (disyuncion)
al_menos_uno = parcial_1 | parcial_2

#Se muestra los resultados
print(f"Aprobaron ambos: {ambos}")
print(f"Aprobaron solo uno: {solo_uno}")
print(f"Aprobaron al menos uno: {al_menos_uno}")

#Ejercicio 8: Gestión de stock de productos
#Se crea un diccionario con productos y su stock inicial
stock_productos = {
    "Gaseosa": 10,
    "Jugo": 15,
    "Aderezo": 20
}

producto = input("Ingresá el producto a consultar o agregar: ")

#Verificamos si el producto ya existe en el diccionario
if producto in stock_productos:
    print(f"Stock actual de {producto}: {stock_productos[producto]}")
    agregar = int(input("¿Cuántas unidades quiere agregar?: "))  #Se pide unidades a agregar
    stock_productos[producto] += agregar  #Se suma al stock existente
    print(f"Nuevo stock de {producto}: {stock_productos[producto]}")
else:
    #Si el producto no existe, lo agregamos con un stock inicial ingresado por el usuario
    nuevo_stock = int(input(f"Producto no encontrado. Ingresá stock inicial para {producto}: "))
    stock_productos[producto] = nuevo_stock
    print(f"{producto} agregado con stock {nuevo_stock}")

#Ejercicio 9: Agenda con tuplas como clave
#Se crea una agenda donde la clave es una tupla (día y hora)
agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "18:30"): "Gimnasio"
}

dia = input("Ingresá el día a consultar: ")  #Se pide el día
hora = input("Ingresá la hora a consultar (HH:MM): ")  #Se pide la hora

#Se busca la actividad correspondiente en la agenda
actividad = agenda.get((dia.lower(), hora))  #la funcion .lower() evita errores de mayusculas
if actividad:
    print(f"Actividad programada: {actividad}")
else:
    print("No hay actividad programada para ese horario.")

#Ejercicio 10: Invertir un diccionario de países y capitales
#Se crea un diccionario donde las claves son países y los valores sus capitales
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Brasil": "Brasilia"
}

#Se invierte el diccionario usando comprensión: clave pasa a valor y viceversa
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

#Se muestra el nuevo diccionario invertido
print("Diccionario invertido:")
print(capitales_paises)
