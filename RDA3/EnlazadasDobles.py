# Clase NodoDoble
class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

# Clase HistorialNavegador
class HistorialNavegador:
    def __init__(self):
        self.actual = None  # Nodo donde se encuentra el usuario

    def visitar_pagina(self, url):
        nuevo_nodo = NodoDoble(url)
        if self.actual is not None:
            # Eliminar páginas siguientes
            self.actual.siguiente = None
            nuevo_nodo.anterior = self.actual
            self.actual.siguiente = nuevo_nodo
        self.actual = nuevo_nodo

    def atras(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
        else:
            print("No hay página anterior.")

    def adelante(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
        else:
            print("No hay página siguiente.")

    def mostrar_historial(self):
        # Ir al inicio del historial
        nodo = self.actual
        while nodo and nodo.anterior:
            nodo = nodo.anterior
        print("Historial de navegación:")
        while nodo:
            indicador = "<-- actual" if nodo == self.actual else ""
            print(f"- {nodo.dato} {indicador}")
            nodo = nodo.siguiente

    def pagina_actual(self):
        return self.actual.dato if self.actual else None

# Bloque de prueba
navegacion = HistorialNavegador()

navegacion.visitar_pagina("stackoverflow.com")
navegacion.visitar_pagina("openai.com")
navegacion.visitar_pagina("github.com")

navegacion.atras()
navegacion.atras()

navegacion.visitar_pagina("google.com")

navegacion.mostrar_historial()
print("Página actual:", navegacion.pagina_actual())
