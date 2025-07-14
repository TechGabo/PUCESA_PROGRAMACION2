# Definimos la clase ColaPrioridadHospital (sin usar deque)
class ColaPrioridadHospital:
    def __init__(self):
        # Usamos una lista para almacenar los pacientes como tuplas (prioridad, nombre)
        self.items = []

    def encolar(self, paciente, prioridad):
        # Agrega un paciente a la cola con su prioridad
        # La prioridad más urgente es 1, la menos urgente es 4
        self.items.append((prioridad, paciente))
        print(f"Se agregó: {paciente} (Prioridad {prioridad})")
        
    def desencolar(self):
        # Atiende al paciente con mayor prioridad (número más bajo)
        if not self.esta_vacia():
            # Buscar índice del paciente con menor número de prioridad
            indice_prioridad = 0
            for i in range(1, len(self.items)):
                if self.items[i][0] < self.items[indice_prioridad][0]:
                    indice_prioridad = i
            
            # Eliminar y devolver al paciente
            prioridad, paciente = self.items.pop(indice_prioridad)
            print(f"Se atendió: {paciente} (Prioridad {prioridad})")
            return paciente
        else:
            print("No hay pacientes por atender.")
            return None

    def esta_vacia(self):
        # Retorna True si la cola está vacía
        return len(self.items) == 0

    def tamaño(self):
        # Devuelve cuántos pacientes están en espera
        return len(self.items)

    def ver_primero(self):
        # Retorna el primer paciente que sería atendido por prioridad
        if not self.esta_vacia():
            indice_prioridad = 0
            for i in range(1, len(self.items)):
                if self.items[i][0] < self.items[indice_prioridad][0]:
                    indice_prioridad = i
            return self.items[indice_prioridad]
        else:
            return None

    def mostrar_pendientes(self):
        # Muestra todos los pacientes ordenados por prioridad
        if self.esta_vacia():
            print("No hay pacientes en espera.")
            return

        print("\n***** Pacientes pendientes (ordenados por prioridad): *****")
        # Ordenamos temporalmente para mostrar, sin alterar el orden real de llegada
        ordenados = sorted(self.items, key=lambda x: x[0])
        for prioridad, paciente in ordenados:
            print(f"- {paciente} (Prioridad {prioridad})")


#Simulación
# Creamos la cola de prioridad del hospital
hospital = ColaPrioridadHospital()

# Encolamos al menos 8 pacientes con diferentes prioridades
hospital.encolar("Gabriel", 2)
hospital.encolar("Ana", 1)
hospital.encolar("Beatriz", 3)
hospital.encolar("Javier", 4)
hospital.encolar("Elena", 1)
hospital.encolar("Juan", 2)
hospital.encolar("Gabriela", 3)
hospital.encolar("Alejandro", 2)

# Mostramos los pacientes pendientes antes de atender
hospital.mostrar_pendientes()
print(f"\nTotal de pacientes en espera: {hospital.tamaño()}")

# Atendemos a todos los pacientes uno por uno
print("\n*** Atendiendo pacientes ***")
while not hospital.esta_vacia():
    hospital.desencolar()

print("\t\nTodos los pacientes han sido atendidos.")
