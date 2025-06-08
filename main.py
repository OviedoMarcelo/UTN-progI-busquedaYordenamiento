import ordenamiento
from busqueda import busqueda_lineal, busqueda_binaria
import random

def main():
    # Crear datos de prueba
    tamanos = [10, 1000, 100000]
    
    for tamano in tamanos:
        print(f'\n--- Prueba con {tamano} elementos ---')
        # podemos llamar primero a un algoritmo de ordenamiento de marce
        # y eliminar el sorted
        # range(num) devuelve una secuencia desde 0 hasta num -1
        # random.sample(secuencia, cantidad) devuelve una lista con la cantidad de elementos especificados
        # pertenecientes a la secuencia específicada 
        datos = sorted(random.sample(range(tamano * 10), tamano))
        objetivo = random.choice(datos)  # Objetivo que existe
        
        # Búsqueda lineal
        indice_lineal, tiempo_lineal = busqueda_lineal(datos, objetivo)
        print(f'Búsqueda lineal: Índice {indice_lineal}, Tiempo {tiempo_lineal:.6f} segundos')
        
        # Búsqueda binaria
        indice_binario, tiempo_binario = busqueda_binaria(datos, objetivo)
        print(f'Búsqueda binaria: Índice {indice_binario}, Tiempo {tiempo_binario:.6f} segundos')

        # LLAMAR A LOS ORDENAMIENTOS CON OTRAS LISTAS DESORDENADAS:


main()
