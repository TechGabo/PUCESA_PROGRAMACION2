
# Parte 1: Explicación conceptual

#1. Búsqueda lineal:
#Es un método de búsqueda que recorre una lista elemento por elemento desde el principio hasta el final.
#Compara cada elemento con el valor buscado. Es fácil de implementar y no requiere que la lista esté ordenada.
#Sin embargo, puede ser ineficiente para listas largas, ya que en el peor caso revisa todos los elementos.

#2. Búsqueda binaria:
#Es un método eficiente para buscar en listas ordenadas. Divide la lista a la mitad y compara el valor medio
#con el objetivo. Si no hay coincidencia, decide en qué mitad continuar la búsqueda. Repite el proceso hasta
#encontrar el elemento o agotar las opciones. Es mucho más rápido que la búsqueda lineal en listas grandes.

#3. ¿Cuándo usar cada una?
#Usa búsqueda lineal si la lista no está ordenada o es pequeña. Usa búsqueda binaria si tienes una lista ordenada
#y necesitas eficiencia, especialmente con grandes cantidades de datos.

# Parte 2: Desarrollo práctico

def busqueda_lineal(lista, objetivo):
    comparaciones = 0
    for i, elemento in enumerate(lista):
        comparaciones += 1
        if elemento.lower() == objetivo.lower():
            return i, comparaciones
    return -1, comparaciones

def busqueda_binaria(lista_ordenada, objetivo):
    inicio = 0
    fin = len(lista_ordenada) - 1
    comparaciones = 0
    while inicio <= fin:
        comparaciones += 1
        medio = (inicio + fin) // 2
        if lista_ordenada[medio].lower() == objetivo.lower():
            return medio, comparaciones
        elif lista_ordenada[medio].lower() < objetivo.lower():
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1, comparaciones

# Lista de productos
productos = [
    "Proyector", "Celular", "Webcam", "Router", "Teclado",
    "Tablet", "Cargador", "Altavoz", "Cámara", "Control remoto",
    "Audífonos", "Laptop", "Memoria USB", "Micrófono", "Disco Duro",
    "Smartwatch", "Monitor", "Batería externa", "Mouse", "Impresora"
]

# Lista ordenada para búsqueda binaria
productos_ordenados = sorted(productos)

# Historial de búsquedas
historial = []

while True:
    print("\tDispositivos Electrónicos")
    buscar = input("Ingrese el nombre del producto a buscar(o presione Enter para salir): ").strip()
    if buscar == "":
        print("Finalizando búsqueda...")
        break

    # Búsqueda lineal
    pos_lineal, comp_lineal = busqueda_lineal(productos, buscar)

    # Búsqueda binaria
    pos_binaria, comp_binaria = busqueda_binaria(productos_ordenados, buscar)
    print("\t\nResultados:")
    if pos_lineal != -1:
        print(f"{buscar} encontrado con búsqueda lineal en posición {pos_lineal} ({comp_lineal} comparaciones).")
        print(f"{buscar} encontrado con búsqueda binaria en posición {pos_binaria} lista ordenada ({comp_binaria} comparaciones).")
    else:
        print(f"'{buscar}' no se encuentra en el catálogo.")
        print(f"Comparaciones realizadas Lineal: {comp_lineal}, Binaria: {comp_binaria}")

    historial.append({
        "producto": buscar,
        "encontrado": pos_lineal != -1,
        "comparaciones_lineal": comp_lineal,
        "comparaciones_binaria": comp_binaria
    })

# Mostrar resumen final
for i, entrada in enumerate(historial, 1):
    if entrada["encontrado"]:
        estado = "Encontrado"
    else:
        estado = "No encontrado"
    print(f"{i}. {entrada['producto']}: {estado} | Lineal: {entrada['comparaciones_lineal']} | Binaria: {entrada['comparaciones_binaria']}")

