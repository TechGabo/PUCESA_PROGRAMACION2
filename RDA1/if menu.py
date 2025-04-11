# Menú de opciones
print("Menú de opciones:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Salir")

opcion = int(input("Elige un número del menú (1-4): "))

# Verificacion 
if opcion < 1 and opcion > 4:
    print("Error: opción no válida")
    
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    # Operaciones
    if opcion == 1:
        print("\tSuma")
        suma = num1 + num2
        print(f"La suma es: {suma}")
    
    elif opcion == 2:
        print("\tResta")
        resta = num1 - num2
        print(f"La resta es: {resta}")
    
    elif opcion == 3:
        print("\tMultiplicación")
        multiplicacion = num1 * num2
        print(f"La multiplicación es: {multiplicacion}")
    
    elif opcion == 4:
        print("\tDivisión")
        if num2 == 0:
            print("Error: No se puede dividir por cero.")
        else:
            division = num1 / num2
            print(f"La división es: {division}")
else:
    print("Saliendo del programa...")



##############################################################################      
print("\tMENU")  
print("\tSeleccionar opciones")
print("1. Ingresa por teclado 2 numeros verifique el tipo de dato")
print("2. Validar que el segundo numero no sea cero")
print("3. Realizar la operacion seleccionada")
print("4. Mostrar el resultado")
print("5. Validar que la operacion seleccionada sea correcta")
print("6. Mostrar un mensaje de error si la operacion no es correcta")
print("7. Salir")

opcion = int(input("Elige una opción (1-8): "))

if opcion == 1:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if num1:
        print(f"Números ingresados correctamente: {num1}, {num2}")
    else:
        print("Error: Uno de los valores ingresados no es un número válido.")

if opcion == 2:
    if num2 == 0:
        print("Error: El segundo número no puede ser cero.")
    else:
        print("El segundo número es válido.")

if opcion == 4:
    print("\tSelecciona la operación:")
    resultado = num1 + num2
    print(f"La suma es: {resultado}")
    
    resultado = num1 - num2
    print(f"La resta es: {resultado}")

    resultado = num1 * num2
    print(f"La multiplicación es: {resultado}")

    if num1 == 0:
        print("Error: No se puede dividir por cero.")
    else:
        resultado = num1 / num2
        print(f"La división es: {resultado}")

if opcion == 5:
    

#if opcion == 6:
    

#if opcion == 7:
    print("Si se ingresa una opción incorrecta, se mostrará un mensaje de error.")

if opcion == 8:
    print("Saliendo del programa...")