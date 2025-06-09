#Crea una lista de al menos 10 clientes representados como tuplas:
#Formato: (nombre_cliente, saldo)
#clientes = [("Carlos", 100.0), ("Ana", 50.5), ...]
#(nombre_cliente, saldo)

#Crea una lista de al menos 10 clientes representados como tuplas
clientes = [("Carlos", 100.0), ("Ana", 50.5), ("Juan", 80.0),
           ("Beatriz", 75.3), ("David", 200.0), ("Elena", 10.0),
           ("Fernando", 150.0), ("Gabriela", 20.0), ("Hugo", 300.0),
           ("Irene", 5.0)]  
# Crea una función para ordenar la lista de clientes por nombre usando Insertion Sort
def insertion_sort_por_nombre(lista):
    lista = lista.copy()
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j][0] > clave[0].lower():
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

# Crea una función para ordenar la lista de clientes por saldo usando Selection Sort
def selection_sort_por_saldo(lista):
    lista = lista.copy()
    for i in range(len(lista)):
        min_idx = i
        for j in range(i + 1, len(lista)):
            if lista[j][1] < lista[min_idx][1]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista