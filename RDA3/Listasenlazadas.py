class NodoPersona:
    def __init__(self, nombre, turno):
        self.nombre = nombre
        self.turno = turno
        self.siguiente = None

# Clase para gestionar la cola de atención (como banco o centro médico)
class ColaAtencionClientes:
    def __init__(self):
        self.primero = None

    def insertar(self, nombre, turno):
        nueva_persona = NodoPersona(nombre, turno)
        if self.primero is None:
            self.primero = nueva_persona
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva_persona
        print(f"Cliente agregado: {nombre} (Turno {turno})")

    def eliminar(self):
        if self.primero:
            atendido = self.primero
            self.primero = self.primero.siguiente
            print(f"Cliente atendido: {atendido.nombre} (Turno {atendido.turno})")
        else:
            print("No hay clientes en espera.")

    def mostrar(self):
        if not self.primero:
            print("No hay clientes en la cola.")
        else:
            actual = self.primero
            print("Clientes en espera:")
            while actual:
                print(f"- {actual.nombre} (Turno {actual.turno})")
                actual = actual.siguiente

# Clase Nodo para páginas web
class NodoPagina:
    def __init__(self, url):
        self.url = url
        self.anterior = None
        self.siguiente = None

# Clase para gestionar historial como navegador web
class HistorialNavegador:
    def __init__(self):
        self.actual = None

    def insertar(self, url):
        nueva_pagina = NodoPagina(url)
        if self.actual is not None:
            self.actual.siguiente = None  # Borrar el "futuro"
            nueva_pagina.anterior = self.actual
            self.actual.siguiente = nueva_pagina
        self.actual = nueva_pagina
        print(f"Página visitada: {url}")

    def retroceder(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            print(f"Retrocediste a: {self.actual.url}")
        else:
            print("No puedes retroceder más.")

    def avanzar(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            print(f"Avanzaste a: {self.actual.url}")
        else:
            print("No puedes avanzar más.")

    def mostrar(self):
        nodo = self.actual
        while nodo and nodo.anterior:
            nodo = nodo.anterior
        print("Historial de navegación:")
        while nodo:
            indicador = "<-- actual" if nodo == self.actual else ""
            print(f"- {nodo.url} {indicador}")
            nodo = nodo.siguiente

print("\t***Simulación de Cola de Atención (Lista Simple)***")
cola = ColaAtencionClientes()
cola.insertar("Carlos", 101)
cola.insertar("Ana", 102)
cola.insertar("Luis", 103)
cola.insertar("María", 104)
cola.insertar("Jorge", 105)

cola.mostrar()
cola.eliminar()
cola.eliminar()
cola.mostrar()


