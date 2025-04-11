#input
nombre= input("¿Cual es tu nombre: ")
edad=int(input("¿Cual es tu edad: "))
altura=float(input("¿Cuanto mides?: "))
print(f"Hola{nombre} tienes {edad} años")
print(f"Mides {altura} metros")
############################################
#operaciones
num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))
suma= num1 + num2
resta= num1 - num2
multiplicacion= num1 * num2
divicion= num1 / num2
potencia= num1 ** num2
divicion_entera= num1//num2
modulo=num1%num2

print("La suma es:" ,suma)
print("La resta es:",resta)
print("La multiplicacion es:",multiplicacion)
print("La division es:",divicion)
print("La potencia es:",potencia)
print("La division entera es:",divicion_entera)
print("El modulo es:",modulo)

#####################################################
a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))
c=int(input("Ingrese el tecer numero: "))
#####################################
#if
if a>b:
    print("a es mayor que b")
else:
    print("a no es mayor que b")
    
#######################
#elif
if a>b:
    print("a es mayor que b")
elif a==b:
    print("a es igual que b")
else:
    print("a no es mayor que b")
########################################
#if compuesto
if a>b:
    print("a es mayor que b")
    if a>c:
        print("a es mayor que c")
    else:
        print("a no es mayor que c")
else:
    print("a no es mayor que b")
    if a>c:
        print("a es mayor que c")
    else:
        print("a no es mayor que c")
#################################################################
        
a=5
b=0
if b==0:
    print("ERROR: No se puede dividir entre cero")
else:
    print(a/b)
#--------------------------------------------------------------
if b!=0:
    print(a/b)
else:
    print("Error: Divicion por cero")
#-------------------------------------------------------------
if b==0:print("Eroor: Divicion por cero")
else:print(a/b)
#-------------------------------------------------------------

