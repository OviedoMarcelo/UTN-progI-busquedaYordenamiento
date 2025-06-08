import time

def busqueda_lineal(lista, objetivo):
    """Búsqueda lineal (O(n)) que devuelve (índice, tiempo)"""
    inicio = time.perf_counter()
    
    for i in range(len(lista)):  
        if lista[i] == objetivo: 
            fin = time.perf_counter()
            return i, fin - inicio
    
    fin = time.perf_counter()
    return -1, fin - inicio

def busqueda_binaria(lista, objetivo):
    """Búsqueda binaria (O(log n)) que devuelve (índice, tiempo)"""
    inicio = time.perf_counter()
    izquierda, derecha = 0, len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valor_medio = lista[medio]
        
        if valor_medio == objetivo:
            fin = time.perf_counter()
            return medio, fin - inicio
        elif valor_medio < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    fin = time.perf_counter()
    return -1, fin - inicio
