# Parte 1: Implementación
import random
# Función para imprimir resultados de rendimiento
def mostrar_resultados(nombre, lista_ordenada, comparaciones, intercambios):
    print(f"\t{nombre}")
    print("Lista ordenada:", lista_ordenada)
    print(f"Comparaciones: {comparaciones}")
    print(f"Intercambios: {intercambios}")

# Algoritmo 1: Bubble Sort
def bubble_sort(lista):
    lista = lista.copy()
    n = len(lista)
    comparaciones = 0
    intercambios = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            comparaciones += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambios += 1
    return lista, comparaciones, intercambios

# Algoritmo 2: Insertion Sort
def insertion_sort(lista):
    lista = lista.copy()
    comparaciones = 0
    intercambios = 0
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > actual:
            comparaciones += 1
            lista[j + 1] = lista[j]
            j -= 1
            intercambios += 1
        lista[j + 1] = actual
        comparaciones += 1  # comparación final falsa
    return lista, comparaciones, intercambios

# Algoritmo 3: Selection Sort
def selection_sort(lista):
    lista = lista.copy()
    comparaciones = 0
    intercambios = 0
    for i in range(len(lista)):
        min_idx = i
        for j in range(i + 1, len(lista)):
            comparaciones += 1
            if lista[j] < lista[min_idx]:
                min_idx = j
        if min_idx != i:
            lista[i], lista[min_idx] = lista[min_idx], lista[i]
            intercambios += 1
    return lista, comparaciones, intercambios

# Lista de precios (aleatoria)
precios = [89, 34, 12, 78, 45, 23, 56, 10, 67, 38]

# Mostrar lista original
print("Lista original de precios:", precios)

# Aplicar Bubble Sort
orden_bubble, comp_b, interc_b = bubble_sort(precios)
mostrar_resultados("Bubble Sort", orden_bubble, comp_b, interc_b)

# Aplicar Insertion Sort
orden_insertion, comp_i, interc_i = insertion_sort(precios)
mostrar_resultados("Insertion Sort", orden_insertion, comp_i, interc_i)

# Aplicar Selection Sort
orden_selection, comp_s, interc_s = selection_sort(precios)
mostrar_resultados("Selection Sort", orden_selection, comp_s, interc_s)

# Parte extra: permitir ingreso de precios
respuesta = input("\n¿Deseas ingresar tus propios precios? (s/n): ").lower()
if respuesta == "s":
    precios_personal = input("Introduce los precios separados por comas: ")
    try:
        lista_usuario = [float(x.strip()) for x in precios_personal.split(",")]
        print("\nLista ingresada:", lista_usuario)

        orden_bubble, comp_b, interc_b = bubble_sort(lista_usuario)
        mostrar_resultados("Bubble Sort", orden_bubble, comp_b, interc_b)

        orden_insertion, comp_i, interc_i = insertion_sort(lista_usuario)
        mostrar_resultados("Insertion Sort", orden_insertion, comp_i, interc_i)

        orden_selection, comp_s, interc_s = selection_sort(lista_usuario)
        mostrar_resultados("Selection Sort", orden_selection, comp_s, interc_s)

    except ValueError:
        print("¡Error! Asegúrate de ingresar solo números separados por comas.")

# Parte extra 2: listas en distintos órdenes
ordenes = {
    "Ascendente": sorted(precios),
    "Descendente": sorted(precios, reverse=True),
    "Aleatorio": random.sample(precios, len(precios))
}

print("\tComparación por tipo de orden de la lista")
for tipo, lista in ordenes.items():
    print(f"\nLista en orden {tipo}: {lista}")
    lista_bubble, comparaciones_bubble, intercambios_bubble = bubble_sort(lista)
    lista_insertion, comparaciones_insertion, intercambios_insertion = insertion_sort(lista)
    lista_selection, comparaciones_selection, intercambios_selection = selection_sort(lista)
    print(f"Comparaciones Bubble: {comp_b} | Inserción: {comp_i} | Selección: {comp_s}")
    
#---------------------------------------------------------------------------------------------------------------------
#En una celda Markdown (o comentario si es script):
#Explica cómo funciona cada algoritmo (brevemente, en tus propias palabras).
#-Bubble Sort
#Este algoritmo compara pares de elementos adyacentes y los intercambia si están en el orden incorrecto. 
#Repite este proceso varias veces hasta que toda la lista esté ordenada. Es fácil de entender, pero puede hacer muchas 
#comparaciones innecesarias.

#-Insertion Sort
#Ordena la lista construyendo una sublista ordenada a medida que recorre los elementos. 
#Inserta cada nuevo elemento en su posición correcta dentro de la parte ya ordenada. 
#Es eficiente para listas pequeñas o casi ordenadas.

#-Selection Sort
#Busca el valor mínimo en la lista y lo coloca en la primera posición, luego el segundo menor, y así sucesivamente. 
#Hace menos intercambios que Bubble Sort, pero igual realiza muchas comparaciones.

#---------------------------------------------------------------------------------------------------------------------
#Compara sus rendimientos: ¿Cuál fue más eficiente en tu caso y por qué?
#En mi prueba con una lista de 10 precios, Insertion Sort fue el más eficiente en cuanto a comparaciones y, 
#a veces, intercambios, especialmente si la lista estaba casi ordenada. 
#Bubble Sort hizo muchas más comparaciones, y Selection Sort tuvo un rendimiento medio, aunque realiza menos intercambios.

#---------------------------------------------------------------------------------------------------------------------
#¿En qué situaciones usarías cada uno en la vida real o en software?
#-Bubble Sort: Bueno para enseñar algoritmos básicos, pero no recomendable en aplicaciones reales.
#-Insertion Sort: Útil cuando los datos ya están casi ordenados o en listas pequeñas.
#-Selection Sort: Apto cuando el número de intercambios debe mantenerse bajo, aunque no es el más rápido.