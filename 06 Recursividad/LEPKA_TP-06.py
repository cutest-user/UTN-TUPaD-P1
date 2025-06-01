#Alumno: LEPKA AGUSTIN MARIO NICOLAS
#Comision: 25

#Actividad 1: Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario

def factorial(n):
    """
    Se aplica recursividad en una funcion para calcular el factorial de un número entero positivo n.
    El factorial de n (n!) es el producto de todos los enteros desde 1 hasta n.
    Caso base: factorial(1) = 1
    Caso recursivo: factorial(n) = n * factorial(n-1)
    """
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

#Actividad 2: Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def fibonacci(pos):
    """
    Se aplica recursividad en una funcion para calcular el valor de Fibonacci en la posición 'pos'.
    Serie de Fibonacci: 0, 1, 1, 2, 3, 5, 8, ...
    Caso base:

    fibonacci(0) = 0
    fibonacci(1) = 1

    Caso recursivo:

    fibonacci(pos) = fibonacci(pos-1) + fibonacci(pos-2)
    """
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

#Actividad 3: Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general.

def potencia(base, exponente):
    """
    Se aplica recursividad en una funcion para calcular base elevado a la potencia exponente.
    Caso base: potencia(base, 0) = 1
    Caso recursivo: potencia(base, exponente) = base * potencia(base, exponente-1)
    """
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

#Actividad 4:Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(n):
    """
    Se aplica recursividad en una funcion que convierte un número decimal entero positivo a su representación binaria en forma de cadena.
    Proceso:
    Dividir el número por 2 y guardar el resto (0 o 1).
    Repetir con el cociente hasta que sea 0.
    Leer los restos de abajo hacia arriba para formar el número binario.

    Caso base: Si n es 0, devolver cadena vacía (porque no hay más divisiones).
    Caso recursivo: decimal_a_binario(n // 2) + str(n % 2)
    """
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

#Actividad 5:Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.

def es_palindromo(palabra):
    """
    Se aplica recursividad en una funcion para determinar si una palabra es palíndromo.
    Un palíndromo es una palabra que se lee igual de adelante hacia atrás.
    Caso base:
    Si la palabra tiene 0 o 1 caracteres, es palíndromo.

    Caso recursivo:
    Comparar primer y último carácter; si coinciden, llamar recursivamente con la palabra sin esos caracteres.
    """
    if len(palabra) <= 1:
        return True
    else:
        if palabra[0] == palabra[-1]:
            return es_palindromo(palabra[1:-1])
        else:
            return False

#Actividad 6: Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(n):
    """
    Se aplica recursividad en una funcion que suma los dígitos de un número entero positivo sin convertirlo a cadena.
    Caso base: si n < 10, devolver n
    Caso recursivo: sumar último dígito + suma_digitos(n // 10)
    """
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

#Actividad 7: Un niño está construyendo una pirámide con cantidad_bloques. En el nivel más bajo coloca n cantidad_bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.

def contar_bloques(n):
    """
    Se aplica recursividad en una funcion que calcula el total de cantidad_bloques necesarios para construir una pirámide.
    Pirámide: nivel inferior con n cantidad_bloques, siguiente con n-1, y así hasta 1 bloque.
    Caso base: si n == 1, retorna 1
    Caso recursivo: n + contar_bloques(n-1)
    """
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

#Actividad 8: Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    """
    Se aplica recursividad en una funcion que cuenta cuántas veces aparece un dígito específico dentro de un número entero positivo.
    Caso base: si el número es 0, no quedan dígitos para contar.
    Caso recursivo: 
    Si el último dígito coincide, sumar 1 + resultado para el resto del número.
    Si no coincide, solo devolver resultado para el resto del número.
    """
    if numero == 0:
        return 0
    else:
        ultimo_digito = numero % 10
        if ultimo_digito == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

#Programa main que llama a todas las funciones

if __name__ == "__main__":

    #Actividad 1:
    #Solicitar al usuario un número entero positivo
    numero_ingresado = int(input("Ingrese un número entero positivo para calcular factoriales hasta ese número: "))
    print("Factoriales del 1 hasta", numero_ingresado)
    for i in range(1, numero_ingresado + 1):
        print(f"{i}! = {factorial(i)}")

    print() #Separador de ejercicios

    #Actividad 2:
    posicion = int(input("Ingrese la posición hasta donde quiere la serie Fibonacci: "))
    print("Serie Fibonacci hasta la posición", posicion)
    for i in range(posicion + 1):
       print(fibonacci(i), end=" ")
    print() #Separador de ejercicios

    #Actividad 3:
    base = int(input("Ingrese la base para calcular potencia: "))
    exponente = int(input("Ingrese el exponente: "))
    print(f"{base}^{exponente} = {potencia(base, exponente)}\n")

    #Actividad 4:
    numero_decimal = int(input("Ingrese un número entero positivo para convertir a binario: "))
    # Si el número es 0, el resultado binario es "0"
    binario = decimal_a_binario(numero_decimal) if numero_decimal > 0 else "0"
    print(f"El número {numero_decimal} en binario es: {binario}\n")

    #Actividad 5:

    palabra = input("Ingrese una palabra para verificar si es palíndromo (sin espacios ni tildes): ").lower()
    print(f"¿La palabra '{palabra}' es palíndromo? {es_palindromo(palabra)}\n")

    #Actividad 6:

    numero_para_sumar_digitos = int(input("Ingrese un número entero positivo para sumar sus dígitos: "))
    print(f"La suma de los dígitos de {numero_para_sumar_digitos} es: {suma_digitos(numero_para_sumar_digitos)}\n")

    #Actividad 7:

    cantidad_bloques = int(input("Ingrese la cantidad de cantidad_bloques en el nivel más bajo de la pirámide: "))
    print(f"Total de cantidad_bloques necesarios para la pirámide: {contar_bloques(cantidad_bloques)}\n")

    #Actividad 8:

    numero = int(input("Ingrese un número entero positivo para contar dígitos: "))
    dig = int(input("Ingrese el dígito a contar (0-9): "))
    print(f"El dígito {dig} aparece {contar_digito(numero, dig)} veces en el número {numero}.")
