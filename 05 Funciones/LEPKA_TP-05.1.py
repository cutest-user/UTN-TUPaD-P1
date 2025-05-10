#Alumno: LEPKA AGUSTIN MARIO NICOLAS
#Comision: 25



#Ejercicio 1: Crear una lista con los números del 1 al 100 que sean múltiplos de 4.
#Se usa la función range para generar los múltiplos de 4 entre 1 y 100.

multiplos= list(range(4, 101, 4))
print("Múltiplos de 4 entre 1 y 100:", multiplos)

#Ejercicio 2: Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo.
#Se usa una lista con 5 elementos y se accede al cuarto elemento con indexación negativa (-2).
elementos = ['auto', 'avion', 'barco', 'arbol', 'helicoptero']
cuarto_elemento = elementos[-2]  # Accediendo al penúltimo
print("El penúltimo elemento es:", cuarto_elemento)

#Ejercicio 3: Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.
#Se usa una lista vacía y usamos el método append para agregar elementos.

lista_vacia = []
lista_vacia.append('auto')
lista_vacia.append('avion')
lista_vacia.append('barco')
print("Lista con tres palabras:", lista_vacia)

#Ejercicio 4: Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.
#Se accede y modifica por índice (el segundo es en el índice 1, y el último es -1).

animales = ["elefante", "halcon", "ave", "tiburon"]
animales[1] = "leon" 
animales[-1] = "tigre" 
print("Lista de animales modificada:", animales)

#Ejercicio 5: Explicar el siguiente programa:

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros)) 
print("Lista después de eliminar el valor máximo:", numeros)

#Este programa remueve el valor maximo de la lista "numeros", despues de eso imprime la lista ya modificada.

#Ejercicio 6: Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
#Se usa range con un step de 5 para generar los números solicitados

numeros_10_al_30 = list(range(10, 31, 5))
print("Los dos primeros números son:", numeros_10_al_30[:2])

#Ejercicio 7: Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.

autos = ["ferrari", "lamborghini", "fiat", "renault"]
autos[1] = "volvo"  
autos[2] = "scania" 
print("Lista de autos modificada:", autos)

#Ejercicio 8: Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente.

dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("Lista de dobles:", dobles)

#Ejercicio 9: Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

#a)Se agrega "jugo" a la lista del tercer cliente usando append.

compras[2].append("jugo")

#b)Se reemplaza "fideos" por "tallarines" en la lista del segundo cliente.

compras[1][compras[1].index("fideos")] = "tallarines"

#c)Se elimina "pan" de la lista del primer cliente.

compras[0].remove("pan")

#d)Se imprime la lista modificada por pantalla.

print("Lista de compras modificada:", compras)

#Ejercicio 10: Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#Usamos listas dentro de la lista principal para crear la estructura solicitada.

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

#Posición 0: 15
#Posición 1: True
#Posición 2: Sublista
#Posición 3: False

#Se imprime por pantalla la lista solicitada.
print("Lista anidada:", lista_anidada)
