class PilaTareas:
    def __init__(self):
        # Creamos una lista vacía para usar como pila
        self.items = []

    def agregar_tarea(self, tarea):
        # Agrega una tarea al final de la pila
        self.items.append(tarea)
        print(f"Tarea agregada: {tarea}")

    def terminar_tarea(self):
        # Elimina la última tarea si la pila no está vacía
        if self.tamaño() > 0:
            tarea = self.items.pop()
            print(f"Tarea finalizada: {tarea}")
        else:
            print("No hay tareas por finalizar.")

    def ver_ultima_tarea(self):
        # Muestra la última tarea sin eliminarla
        if self.tamaño() > 0:
            print(f"Última tarea en la pila: {self.items[-1]}")
        else:
            print("No hay tareas en la pila.")

    def tamaño(self):
        # Devuelve cuántas tareas hay en la pila
        return len(self.items)

print