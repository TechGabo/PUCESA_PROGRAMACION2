#Definición de la función de búsqueda binaria
def busqueda_binaria(lista, objetivo):
    inicio = 0 #Índice inicial
    fin = len(lista) - 1 #Indice final
    comparaciones = 0 #Inicializamos el contador de comparaciones

    while inicio <= fin: #Mientras el índice de inicio sea menor o igual al de fin
        comparaciones += 1 #Incrementamos el contador de comparaciones
        medio = (inicio + fin) // 2 #Índice del medio
        if lista[medio] == objetivo: #Si el elemento medio es igual al objetivo
            return medio, comparaciones #Retornamos la posición y el número de comparaciones
        elif lista[medio] < objetivo: #Si el elemento medio es menor al objetivo
            inicio = medio + 1 #Ajustamos el índice de inicio
        else: #Si el objetivo es menor que el valor medio
            fin = medio - 1 #Ajustamos el índice de fin
    return -1, comparaciones #Si no se encuentra el elemento, retornamos -1 y el número de comparaciones

#Lista ordenada de números del 10 al 100
numeros = list(range(10, 101, 10))

#Solicitar al usuario un número
buscar = int(input("Ingrese el número que desea buscar: "))

#Ejecutar búsqueda binaria
posicion, comparaciones = busqueda_binaria(numeros, buscar)

#Resultado donde se muestra la posición y el número de comparaciones
if posicion != -1:
    print(f"El número {buscar} se encontró en la posición {posicion}.")
else:
    print(f"El número {buscar} no se encuentra en la lista.")
print(f"Se hicieron {comparaciones} comparaciones.")
