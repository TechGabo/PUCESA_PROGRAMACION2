class persona:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre= nombre
        self.edad= edad
        self.ocupacion= ocupacion
    def descripcion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Ocupación: {self.ocupacion}"
    
def mostrar_menu():
    print("\tGestión De Persona")
    print("1. Agregar Persona")
    print("2. Mostrar todas las personas")
    print("3. Buscar persona por nombre")
    print("4. Salir")

personas=[]

while True:
    mostrar_menu()
    
    opcion = input("Ingrese la opción que desea realizar: ")
    
    if opcion == "1":
        nombre=input("Ingrese el nombre de la persona: ")
        edad=int(input("Ingrese la edad de la persona: "))
        ocupacion=input("Ingrese la ocupación de la persona: ")
        nueva_persona=persona(nombre, edad, ocupacion)
        personas.append(nueva_persona)
        print(f"\tLa persona {nombre} fue agregada con éxito")
        
    elif opcion == "2":
        if len(personas) > 0:
            print("\n\tLista de Persona")
            for persona in personas:
                print(persona.descripcion())
        else:
            print("No hay personas registradas")
    
    elif opcion == "3":
        if len(personas)>0:
            nombre_buscar=input("Ingrese el nombre de la persona a buscar: ")
            encontrado=False
            for persona in personas:
                if persona.nombre.lower()==nombre_buscar.lower():
                    print("Persona Encontrada")
                    print(persona.descripcion())
                    encontrado=True
                    break
            if not encontrado:
                print(f"No se encontró a {nombre_buscar} en la lista")
        else:
            print("No hay personas registradas")
            
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción no válida. Por favor, ingrese una opción válida")
                
