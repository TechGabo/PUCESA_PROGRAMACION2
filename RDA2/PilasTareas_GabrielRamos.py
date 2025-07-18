class PilaTareas:
    def __init__(self):
        self.items = []

    def agregar_tarea(self, tarea):
        self.items.append(tarea)
        print(f"Tarea agregada: {tarea}")

    def terminar_tarea(self):
        if self.tamaño() > 0:
            tarea = self.items.pop()
            print(f"Tarea finalizada: {tarea}")
        else:
            print("No hay tareas por finalizar.")

    def ver_ultima_tarea(self):
        if self.tamaño() > 0:
            print(f"Última tarea: {self.items[-1]}")
        else:
            print("No hay tareas en la pila.")

    def tamaño(self):
        return len(self.items)

pila = PilaTareas()
def menu_pila():
    

    while True:
        print("***********************")
        print("Gabriel Ramos")
        print("***********************")
        print("\t*** MENÚ: GESTOR DE TAREAS ***")
        print("1. Agregar tarea")
        print("2. Terminar tarea")
        print("3. Ver última tarea")
        print("4. Ver tamaño de la pila")
        print("5. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            for i in range(10):
                tarea = input(f"Ingrese la tarea {i+1}: ")
                pila.agregar_tarea(tarea)

        elif opcion == "2": 
            pila.terminar_tarea()

        elif opcion == "3":
            pila.ver_ultima_tarea()

        elif opcion == "4":
            print(f"Número de tareas en pila: {pila.tamaño()}")

        elif opcion == "5":
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecutar menú
menu_pila()
