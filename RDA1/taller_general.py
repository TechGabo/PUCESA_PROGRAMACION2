print("*" * 40) 
print("\tTaller general RDA2")
print("Realizado por: Gabriel Ramos")
print("*" * 40)

# Lista de clientes como tuplas (nombre, saldo)
clientes = [
    ("Carlos", 100.0),
    ("Ana", 50.5),
    ("Beatriz", 75.0),
    ("David", 120.0),
    ("Elena", 30.0),
    ("Fernando", 90.0),
    ("Gabriel", 200.0),
    ("Hugo", 10.0),
    ("Isabel", 65.5),
    ("Jorge", 150.0)
]

# Mostrar clientes
def mostrar_clientes(lista, titulo):
    print(f"\n{titulo}")
    for cliente in lista:
        print(cliente)

# Ordenamiento por inserción y selección
def insertion_sort_por_nombre(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j][0].lower() > actual[0].lower():
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista

# Ordenamiento por selección basado en saldo
def selection_sort_por_saldo(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j][1] < lista[min_idx][1]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

# Búsqueda binaria y lineal por nombre
def busqueda_binaria_nombre(lista_ordenada, objetivo):
    inicio = 0
    fin = len(lista_ordenada) - 1
    comparaciones = 0

    while inicio <= fin:
        comparaciones += 1
        medio = (inicio + fin) // 2
        nombre = lista_ordenada[medio][0].lower()

        if nombre == objetivo.lower():
            return medio, comparaciones
        elif objetivo.lower() < nombre:
            fin = medio - 1
        else:
            inicio = medio + 1

    return -1, comparaciones

# Búsqueda lineal por nombre
def busqueda_lineal_nombre(lista, objetivo):
    comparaciones = 0
    for i, cliente in enumerate(lista):
        comparaciones += 1
        if cliente[0].lower() == objetivo.lower():
            return i, comparaciones
    return -1, comparaciones

# Mostrar lista original
mostrar_clientes(clientes, "Lista original de clientes:")

# Permitir al usuario ingresar un nuevo cliente
agregar = input("\n¿Deseas agregar un nuevo cliente? (s/n): ").lower()
if agregar == "s":
    nuevo_nombre = input("Nombre del nuevo cliente: ")
    nuevo_saldo = float(input("Saldo del nuevo cliente: "))
    clientes.append((nuevo_nombre, nuevo_saldo))
    print("Cliente agregado correctamente.")

# Preguntar si desea ordenar antes de buscar
ordenar = input("\n¿Deseas ordenar la lista por nombre antes de buscar? (s/n): ").lower()

# Mostrar lista original antes de ordenar
if ordenar == "s":
    clientes_ordenados = insertion_sort_por_nombre(clientes.copy())
    mostrar_clientes(clientes_ordenados, "Clientes ordenados por nombre (insertion sort):")

    nombre_a_buscar = input("\nIngrese el nombre del cliente a buscar: ")
    pos, comps = busqueda_binaria_nombre(clientes_ordenados, nombre_a_buscar)

    if pos != -1:
        print(f"Cliente encontrado: {clientes_ordenados[pos]} en posición {pos}")
    else:
        print("Cliente no encontrado.")
    print(f"Comparaciones realizadas: {comps}")
else:# Si no se desea ordenar, se realiza búsqueda lineal
    nombre_a_buscar = input("Ingrese el nombre del cliente a buscar (sin ordenar): ")
    pos, comps = busqueda_lineal_nombre(clientes, nombre_a_buscar)

    if pos != -1:
        print(f"Cliente encontrado: {clientes[pos]} en posición {pos}")
    else:
        print("Cliente no encontrado.")
    print(f"Comparaciones realizadas: {comps}")

# Mostrar lista ordenada por saldo
clientes_por_saldo = selection_sort_por_saldo(clientes.copy())
mostrar_clientes(clientes_por_saldo, "Clientes ordenados por saldo (selection sort):")

## Preguntas de reflexión
