#Definición de la función de búsqueda lineal
def busqueda_lineal(lista, elemento):
    comparaciones = 0 #Inicializamos el contador de comparaciones
    for i in range(len(lista)): #La lista con un ciclo for
        comparaciones += 1 #Incrementamos el contador de comparaciones
        if lista[i] == elemento: #Si encontramos el elemento
            return i, comparaciones #Retornamos la posición y el número de comparaciones
    return -1, comparaciones

#Lista de frutas
frutas = ["manzana", "naranja", "pera", "piña", "sandia", "uva", "banana", "uva", "limón", "melon"]

#Solicitar al usuario una fruta
buscar = input("Ingrese la fruta que desea buscar: ").lower()

#Ejecutar búsqueda lineal
posicion, comparaciones = busqueda_lineal(frutas, buscar)

#Resultado donde se muestra la posición y el número de comparaciones
if posicion != -1:
    print(f"La fruta '{buscar}' se encontró en la posición {posicion}.") 
else:
    print(f"La fruta '{buscar}' no se encuentra en la lista.")
print(f"Se hicieron {comparaciones} comparaciones.")
