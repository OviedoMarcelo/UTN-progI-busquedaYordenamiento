import ordenamiento
from busqueda import busqueda_lineal, busqueda_binaria
import random

def main():
    # Crear datos de prueba
    tamanos = [10, 1000, 10000]
    opcion=""
    print(f"Bienvenido al programa de búsqueda y ordenamiento")
    while opcion not in ["1", "2", "0"]:
        opcion = input(
            "Ingrese la opción deseada:\n"
            "1 - Ejecutar prueba de algoritmo de búsqueda.\n"
            "2 - Ejecutar prueba de algoritmo de ordenamiento.\n"
            "0 - Finalizar\n"
            "Opción: "
        )
        if opcion not in ["1", "2", "0"]:
            print("❌ Opción inválida. Por favor, ingrese 1, 2 o 0.\n")
        elif opcion == "1":
            for tamano in tamanos:
                print(f'\n--- Prueba con {tamano} elementos ---')
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
        elif opcion == "2":
            for tamano in tamanos:
                print(f'\n--- Prueba con {tamano} elementos---')
                datos = sorted(random.sample(range(tamano * 10), tamano), reverse=True) #Genero la lista siempre en el peor caso, totalmente desordenada
                #Ordenamiento de burbuja
                ordenamiento.bubble_sort(datos.copy())
                #Ordenamiento de inserción
                ordenamiento.insertion_sort(datos.copy())
                #Ordenamiento de selección
                ordenamiento.selection_sort(datos.copy())
        else:
            break
        opcion=""
        print("\n")
    #Fin del programa
    print("--------------------")
    print("Fin del programa 👋")
                
main()  
