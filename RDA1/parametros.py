def funcion(nombre):
    print("Estamos estudiando Python", nombre)
funcion("Gabriel")
print("\n")

#---------------------------------------------------------
print("*"*60)
print("\t Pasos para argumentar a una funcion")
def datos(NOMBRE, APELLIDO):
    print("Estamos estudiando Python", NOMBRE, APELLIDO)
datos("Gabriel","Ramos")#Argumentos posicionales
datos(NOMBRE="Edison", APELLIDO="Montesdeoca")#Argumento nominales
print("\n")

#---------------------------------------------------------
print("*"*60)
print("\t Pasar un número indeterminado de argumentos")
def menu(*platos):
    print("Hoy tenemos: ", end="")
    for plato in platos:
        print(plato, end=", ")
menu("pasta","pizza","lasaña")
print("\n")
#---------------------------------------------------------
print("*"*60)
print("\tArgumentos por defecto")
def bienvenido(nombre, lenguaje= "Python"):
    print("Bienvenido a", lenguaje, nombre + "!")
bienvenido("EMENESES")#Ejemplo con los datos originales de la funcion
bienvenido("EMENESES","PHP")#Ejemplo con cambio de datos en el lenguaje de la funcion
bienvenido("GABRIEL","C#")#Mensaje Personalizado, cambiando los datos de la funcion
print("\n")

#---------------------------------------------------------
print("*"*60)
#ciclos
for i in range(1,4):
    print("Hola mundo", i)
print("*"*60)

for i in range(0,5+1):
    print("Tabla del", i)
    for j in range(0,5+1):
        #print(i,"*",j,"=",i*j)
        for k in range(0,5+1):
            print(i,"*",j,"*",k,"=",i*j*k)
print("\n")
print("*"*60)

for r in[10,200,38]:
    print("El elemento del ciclo",r)
    for i in [1,2,3,4]:
         print(f"{i} * {r} = {i*r}")
print("\n")
print("*"*60)
#---------------------------------------------------------
for i in [0,1,2,3,4,5,6,7,8,9,10]:
    if i%2==0:
        print(f"El número {i} es par.")
    else:
        print(f"El número {i} es impar.")
print("\n")
print("*"*60)
#---------------------------------------------------------
print("Par y Impar por separado")
for i in [0,1,2,3,4,5,6,7,8,9,10]:
    if i%2==0:
        print(f"El número {i} es par.")
        
print("*"*60)

for i in [0,1,2,3,4,5,6,7,8,9,10]:
    if i%2!=0:
        print(f"El número {i} es impar.")

print("\n")
print("*"*60)

def contacto(**info):
    print("Datos del contacto")
    for clave, valor in info.items():
        print(f"{clave} = {valor}")
contacto(nombre="Juan", email="juanronpope@gmail.com", telefono=1234567)
print("\n")
contacto(nombre="Pepito", email="pepecrack777@gmail.com", telefono=1234567, direccion= "Calle 123")

print("\n")
print("*"*60)
print("Funciones Recursivos")
def cuenta_regresiva(numero):
    numero -=1
    if numero > 0:
        print(numero)
        cuenta_regresiva(numero)
    else:
        print("Boooooom!!")
cuenta_regresiva(5)
print("\n")
print("*"*60)

class persona:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre= nombre
        self.edad= edad
        self.ocupacion= ocupacion
    def descripcion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Ocupación: {self.ocupacion}"

#Pedimos al usuario que ingrese sus datos
nombre=input("Ingrese su nombre: ")
edad=int(input("Ingrese su edad: "))
ocupacion=input("Ingrese su ocupacion: ")

#Creamos un objeto de tipo persona con la informacion por el usuario
nueva_persona= persona(nombre, edad, ocupacion)

#Imprimimos la descripcion de la persona
print("\tInformacion de la persona creada")
print(nueva_persona.descripcion())

print("\n")
print("*"*60)

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
                
