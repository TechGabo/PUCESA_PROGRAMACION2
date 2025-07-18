class NodoDoble:
    def __init__(self, dato):
        self.dato= dato
        self.anterior= None
        self.siguiente= None
        
#Cread nodos
nodo1= NodoDoble("A")
nodo2= NodoDoble("B")
nodo3= NodoDoble("C")

#Enlazar nodos
nodo1.siguiente=nodo2
nodo2.anterior= nodo1
nodo2.siguiente=nodo3
nodo3.anterior=nodo2

################################################
#Ejemplo con multiples parametros
class Documentos:
    def __init__(self, nombre, tamaño):
        self.nombre = nombre
        self.tamaño = tamaño
doc1= Documentos("documento1", 100)

################################################
#Ejercicio
class Persona:
    def __init__(self, nombre, edad, correo):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
pt= Persona("Pepe", 20, "pepitogamer@gmail.com")
print(pt.nombre, pt.edad, pt.correo)