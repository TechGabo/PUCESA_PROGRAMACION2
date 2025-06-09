#Diferencia de una lista y una biblioteca
#Una lista es una estructura de datos que permite almacenar una colección de elementos,
#mientras que una biblioteca es un conjunto de funciones y métodos predefinidos que se pueden utilizar para realizar tareas específicas.
#Ejemplo de una lista
lista=[]
#Ejemplo de una biblioteca
dicc={}


lista=[1,2,3,4,5,6,7,8,9,9,10]
lista.remove(9)
print(lista)

#EJEMPLO 2: Calcular la suma de los elementos de una lista
numeros = [5,8,2,9,1]
suma = 0
for numero in numeros:
    suma += numero
print("La suma total:", suma)

#EJEMPLO 3: Contar cuantos números pares hay
numeros = [5,8,2,9,1]
pares=0
for num in numeros:
    if num%2==0:
        pares+=1
print("La cantidad de números pares es:", pares)

#EJEMPLO 4: Contar cuántas veces aparece un número en una lista
numeros = [5,8,2,9,1,5,5]  
num=5
contador=0
for i in numeros:
    if i==num:
        contador+=1
print("El número", num, "aparece", contador, "veces en la lista.")

#EJEMPLO 5: Encontrar el numero mayor
numeros = [5,8,2,9,1,5,5]
mayor = numeros[0]
for num in numeros:
    if num > mayor:
        mayor = num
print("El número mayor es:", mayor)

#EJEMPLO FOR: CREAR DUPLICADO EN FOR, elimina el 
#numeros = [1,2,3,4,5]
#nueva_lista = []
#for i in numeros:
#    if i != 2:
#        nueva_lista.remove(i)
#print(nueva_lista)

############################################
def busqueda_lineal(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i  # Devuelve el índice del elemento encontrado
    return -1  # Devuelve -1 si no se encuentra el elemento
datos=[12,5,8,21,9]
print(busqueda_lineal(datos, 21))  # Devuelve el índice del elemento encontrado
print("*" *20)
###########################################
lista=[4,3,9,4,5,6,7,8,9,10,2,1]
numeros1= sorted(lista) #Ordena la lista de menor a mayor
lista_basura=[]#Saca los duplicados
for num in numeros1:
    if num not in (1,2,3,4,5,6,7,8,9,10):
        lista_basura.append(num)
print("Números ordenados de menor a mayor:", num)
##########################################################
lista=[3,1,5]
for i in range(len(lista)-1):
    for j in range(len(lista) -1-i):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]  # Intercambia los elementos
            print(lista[j], lista[j+1], end=" ")

##########################################################
def busqueda_binario(lista, objetivo):
    inicio= 0
    fin= len(lista)-1
    while inicio <= fin:
        medio= (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio  # Devuelve el índice del elemento encontrado
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1  # Devuelve -1 si no se encuentra el elemento
