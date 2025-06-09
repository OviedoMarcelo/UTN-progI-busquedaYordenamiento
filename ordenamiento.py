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
    Función que ordena recibida la lista con el método burbuja y devuelve una lista ordenada. 
    Comparando cada elemento con su adyacente e intercambiando si es necesario.
    Imprime en consola el tiempo que llevó el ordenamiento y los elementos ordenados.
    """
    n = len(lista) #Obtengo el largo de la lista
    inicio = time.time() #inicializo el tiempo
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    fin = time.time() #obtengo el tiempo al finalizar el ordenamiento
    tiempo_ms = (fin - inicio) * 1000  # Convertierto la diferencia a milisegundos
    print(f"Tiempo de ejecución bubble sort para {n} elementos: {tiempo_ms:.3f} ms")
    return lista


#Ordenamiento de inserción

def insertion_sort(lista):
    """
    Función que ordena la lista recibida con el método de insertion y devuelve una lista ordenada. 
    Este método reconstruye la lista de forma ordenadade izquierda a derecha tomando
    1 elemento a la vez y lo colaca en la posición correcta.
    Imprime en consola el tiempo que llevó el ordenamiento y los elementos ordenados.
    """
    n = len(lista) #Obtengo el largo de la lista
    inicio = time.time() #inicializo el tiempo
    #Inicio el recorrido
    for i in range(1, n):
        actual = lista[i] #Agarro el último elemento no ordenado de la lista para la primera vuelta es el elemento [1] para compara con el [0]
        j = i - 1 #Este J equivale al último elemento ordenado de la lista
        while j >= 0 and lista[j] > actual: #Si no me salgo del array y si el elemento anterior ordenado es mayor empiezo a desplazarlo
            lista[j + 1] = lista[j] 
            j -= 1
        lista[j + 1] = actual #una vez llegada a la posición ordenada correcta intercambio y avanzo al siguiente elemento no ordenado
    #Fin del recorrido    
    fin = time.time() #obtengo el tiempo al finalizar el ordenamiento
    tiempo_ms = (fin - inicio) * 1000  # Convertierto la diferencia a milisegundos
    print(f"Tiempo de ejecución insertion sort para {n} elementos: {tiempo_ms:.3f} ms")
    return lista


#Ordenamiento de selección

def selection_sort(lista):
    """
    Función que ordena la lista recibida con el método de selección y devuelve una lista ordenada.
    Este método selecciona el elemento más pequeño de la lista y lo coloca en la posición que le corresponde.
    Imprime en consola el tiempo que llevó el ordenamiento y los elementos ordenados.s
    """
    n = len(lista)
    inicio = time.time() #inicializo el tiempo
    #Inicio el recorrido
    for i in range(n):  #Recorro todos los elementos del array
        min_index = i   #Index del elemento más pequeño
        for j in range(i + 1, n): #recorro del elemento más pequeño hasta el final
            if lista[j] < lista[min_index]: 
                min_index = j #Guardo el index del elemento más pequeño encontrado en recorrido
        lista[i], lista[min_index] = lista[min_index], lista[i] #Al final algo el intercambi con el mínimo index encontrado en la vuelta
    #Fin del recorrido
    fin = time.time() #obtengo el tiempo al finalizar el ordenamiento
    tiempo_ms = (fin - inicio) * 1000  # Convertierto la diferencia a milisegundos
    print(f"Tiempo de ejecución selection sort para {n} elementos: {tiempo_ms:.3f} ms")
    return lista