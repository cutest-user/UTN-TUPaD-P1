#Trabajo integrador - Algoritmos de busqueda y Ordenamiento.
#Alumnos: Frank Rojas (Comision 20) - Agustin Mario Nicolas Lepka (Comision 25)


import random  #Módulo para generar números aleatorios
import time    #Módulo para medir tiempos de ejecución

#Algoritmos de ordenamiento

#Quick Sort
def quick_sort(lista_desordenada):
    #Caso base: si la lista tiene 0 o 1 elementos, ya está ordenada
    if len(lista_desordenada) <= 1:
        return lista_desordenada

    #Se elige el pivote (el elemento central de la lista)
    indice_pivote = len(lista_desordenada) // 2
    elemento_pivote = lista_desordenada[indice_pivote]

    #Se dividen los elementos en tres listas: menores, iguales y mayores al pivote
    sublista_menores = [x for x in lista_desordenada if x < elemento_pivote]
    sublista_iguales = [x for x in lista_desordenada if x == elemento_pivote]
    sublista_mayores = [x for x in lista_desordenada if x > elemento_pivote]

    #Se aplica recursión a menores y mayores, y se combinan todos
    return quick_sort(sublista_menores) + sublista_iguales + quick_sort(sublista_mayores)

#Insertion Sort - más eficiente que Bubble Sort en listas pequeñas o parcialmente ordenadas
def insertion_sort(lista):
    #Se recorre desde el segundo elemento hasta el final
    for posicion_actual in range(1, len(lista)):
        valor_a_insertar = lista[posicion_actual]  #Elemento que se desea ordenar
        posicion_comparacion = posicion_actual - 1  #Posición previa para comparar

        #Se compara hacia atrás y se mueven los elementos mayores
        while posicion_comparacion >= 0 and lista[posicion_comparacion] > valor_a_insertar:
            lista[posicion_comparacion + 1] = lista[posicion_comparacion]
            posicion_comparacion -= 1

        #Inserta el valor en la posición correcta
        lista[posicion_comparacion + 1] = valor_a_insertar
    return lista

#Algoritmos de busqueda

#Búsqueda binaria - requiere que la lista esté ordenada
def busqueda_binaria(lista_ordenada, valor_buscado):
    indice_inicial = 0  # Inicio del rango de búsqueda
    indice_final = len(lista_ordenada) - 1  # Fin del rango

    #Se repite mientras el rango sea válido
    while indice_inicial <= indice_final:
        indice_medio = (indice_inicial + indice_final) // 2  #Índice central
        elemento_medio = lista_ordenada[indice_medio]  #Elemento en el centro

        if elemento_medio == valor_buscado:
            return indice_medio  #Valor encontrado
        elif elemento_medio < valor_buscado:
            indice_inicial = indice_medio + 1  #Buscar en mitad derecha
        else:
            indice_final = indice_medio - 1  #Buscar en mitad izquierda

    return -1  #No se encontró el valor

#Búsqueda secuencial - no requiere lista ordenada
def busqueda_secuencial(lista, valor_buscado):
    for posicion in range(len(lista)):  # Recorre la lista desde el inicio
        if lista[posicion] == valor_buscado:
            return posicion  # Valor encontrado
    return -1  # Valor no encontrado


#Generación de datos académicos (matrículas y notas)
matriculas = random.sample(range(10000, 50000), 20000)  # Lista de 20000 matrículas únicas
notas = [random.uniform(1.0, 10.0) for _ in range(20000)]  # Lista de 20000 notas aleatorias entre 1.0 y 10.0

#Tests de rendimiento

#Test 1: Ordenar la lista de notas con Quick Sort
inicio_quick = time.time()
notas_ordenadas_quick = quick_sort(notas.copy())  #Se hace una copia para no modificar la original
tiempo_quick_sort = time.time() - inicio_quick  #Se mide el tiempo que tomó ordenar

# Seleccionar un valor de nota que sí existe en la lista para las búsquedas
valor_a_buscar = notas[1234]  #Valor a buscar

#Test 2: Buscar una nota específica usando búsqueda binaria sobre la lista ordenada
inicio_busqueda_binaria = time.time()
posicion_binaria = busqueda_binaria(notas_ordenadas_quick, valor_a_buscar)
tiempo_busqueda_binaria = time.time() - inicio_busqueda_binaria

#Test 3: Ordenar la lista con Insertion Sort
inicio_insertion = time.time()
notas_ordenadas_insertion = insertion_sort(notas.copy())
tiempo_insertion_sort = time.time() - inicio_insertion

#Test 4: Buscar una nota específica en lista desordenada usando búsqueda secuencial
inicio_busqueda_secuencial = time.time()
posicion_secuencial = busqueda_secuencial(notas, valor_a_buscar)
tiempo_busqueda_secuencial = time.time() - inicio_busqueda_secuencial

#Test 5: Búsqueda binaria sobre lista desordenada (no se debe usar así, da resultado incorrecto)
inicio_binaria_mal = time.time()
posicion_binaria_desordenada = busqueda_binaria(notas, valor_a_buscar)
tiempo_binaria_mal = time.time() - inicio_binaria_mal

#Test 6: Búsqueda secuencial sobre lista ordenada (funciona igual)
inicio_secuencial_ordenada = time.time()
posicion_secuencial_ordenada = busqueda_secuencial(notas_ordenadas_quick, valor_a_buscar)
tiempo_secuencial_ordenada = time.time() - inicio_secuencial_ordenada

# Se imprimen los tiempos de ejecución de cada prueba y la posición encontrada (si aplica)
print(f"Quick Sort (20000 elementos): {tiempo_quick_sort:.4f} segundos")
print(f"Insertion Sort (20000 elementos): {tiempo_insertion_sort:.4f} segundos")
print(f"Búsqueda Binaria (ordenada): {tiempo_busqueda_binaria:.6f} segundos - Posición: {posicion_binaria}")
print(f"Búsqueda Binaria (desordenada): {tiempo_binaria_mal:.6f} segundos - Resultado incorrecto: {posicion_binaria_desordenada}")
print(f"Búsqueda Secuencial (desordenada): {tiempo_busqueda_secuencial:.6f} segundos - Posición: {posicion_secuencial}")
print(f"Búsqueda Secuencial (ordenada): {tiempo_secuencial_ordenada:.6f} segundos - Posición: {posicion_secuencial_ordenada}")
