class ColaPrioridadClientes:
    def __init__(self):
        self.items = []

    def agregar_cliente(self, nombre, prioridad):
        cliente = (prioridad, nombre)
        insertado = False
        for i in range(len(self.items)):
            if prioridad < self.items[i][0]:
                self.items.insert(i, cliente)
                insertado = True
                break
        if not insertado:
            self.items.append(cliente)
        print(f"Cliente agregado: {nombre} (Prioridad {prioridad})")

    def atender_cliente(self):
        if self.tamaño() > 0:
            prioridad, nombre = self.items.pop(0)
            print(f"Cliente atendido: {nombre} (Prioridad {prioridad})")
        else:
            print("No hay clientes en espera.")

    def mostrar_pendientes(self):
        if self.tamaño() == 0:
            print("No hay clientes pendientes.")
        else:
            print("Clientes pendientes:")
            for prioridad, nombre in self.items:
                print(f"- {nombre} (Prioridad {prioridad})")

    def tamaño(self):
        return len(self.items)


cola = ColaPrioridadClientes()
while True:
    print("***********************")
    print("Gabriel Ramos")
    print("***********************")
    print("\n*** MENÚ: Atención de Clientes ***")
    print("1. Agregar cliente")
    print("2. Atender cliente")
    print("3. Mostrar pendientes")
    print("4. Ver tamaño de la cola")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre del cliente: ")
        while True:
            try:
                prioridad = int(input("Prioridad (1 = urgente, 4 = leve): "))
                if 1 <= prioridad <= 4:
                    break
                else:
                    print("Prioridad inválida. Debe ser entre 1 y 4.")
            except ValueError:
                print("Por favor, ingresa un número válido.")
        cola.agregar_cliente(nombre, prioridad)

    elif opcion == "2":
        cola.atender_cliente()

    elif opcion == "3":
        cola.mostrar_pendientes()

    elif opcion == "4":
        print(f"Total de clientes en espera: {cola.tamaño()}")

    elif opcion == "5":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
