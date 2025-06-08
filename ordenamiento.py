"""
Este módulo de ordenamiento contiene las 3 funciones más comunes para hacer búsqueda. 
Bubble sort, Insertion Sort y Selection Sort. Además estas funciones van a siempre imprimir por consola el tiempo
que demoraron en hacer el ordenamiento y la cantidad de elementos que tenía la lista ingresada para poder estudiar la
eficiancia de cada algoritmo y poder compararlo.
"""
import time

#Ordenamiento de burbuja

def bubble_sort(lista):
    """
    Función que ordena la lista con el método burbuja. 
    Comparando cada elemento con su adyacente e intercambiando si es necesario.
    """
    n = len(lista) #Obtengo el largo de la lista
    inicio = time.time() #inicializo el tiempo
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    fin = time.time() #obtengo el tiempo al finalizar el ordenamiento
    tiempo_ms = (fin - inicio) * 1000  # Convertierto la diferencia a milisegundos
    print(f"Tiempo de ejecución bubble sort para {len} elementos: {tiempo_ms:.3f} ms")
    return lista


#Ordenamiento de inserción

def insertion_sort(lista):
    """
    Función que ordena la lista con el método de insertion. 
    Este método reconstruye la lista de forma ordenadade izquierda a derecha tomando
    1 elemento a la vez y lo colaca en la posición correcta.
    """
    n = len(lista) #Obtengo el largo de la lista
    inicio = time.time() #inicializo el tiempo
    #Inicio el recorrido
    for i in range(1, n):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    #Fin del recorrido    
    fin = time.time() #obtengo el tiempo al finalizar el ordenamiento
    tiempo_ms = (fin - inicio) * 1000  # Convertierto la diferencia a milisegundos
    print(f"Tiempo de ejecución bubble sort para {len} elementos: {tiempo_ms:.3f} ms")
    return lista


#Ordenamiento de selección

def selection_sort(lista):
    """
    Función que ordena la lista con el método de selección. 
    Este método selecciona el elemento más pequeño de la lista y lo coloca en la posición que le corresponde.
    """
    n = len(lista)
    inicio = time.time() #inicializo el tiempo
    #Inicio el recorrido
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    #Fin del recorrido
    fin = time.time() #obtengo el tiempo al finalizar el ordenamiento
    tiempo_ms = (fin - inicio) * 1000  # Convertierto la diferencia a milisegundos
    print(f"Tiempo de ejecución bubble sort para {len} elementos: {tiempo_ms:.3f} ms")
    return lista