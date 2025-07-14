# Crea una lista vacía llamada historial
historial = []

# Insertamos elementos
historial.append("www.google.com")  
historial.append("www.python.org")
historial.append("www.stackoverflow.com")


# Menú de opciones
while True:
    print("***********************")
    print("Gabriel Ramos")
    print("***********************")
    print("\tMenú de opciones:")
    print("1. Historial")
    print("2. Verificar")
    print("3. Ultimo eliminado")
    print("4. Historial vacio")
    print("5. Salir")

    opcion = int(input("Elige un número del menú (1-5): "))

    if opcion < 1 or opcion > 5:
        print("Error: opción no válida")
        continue  # Volver al inicio del bucle

    if opcion == 1:
        print("Historial:", historial)
        
    elif opcion == 2:
        # Verificamos si hay elementos
        if historial:
            print("Página actual:", historial[-1])  # peek
        else:
            print("No hay páginas en el historial")
    
    elif opcion == 3:
        # Elimina la última página visitada y muestra el historial restante
        if historial:
            eliminada = historial.pop()
            print("Volviste desde:", eliminada)
            print("Página actual:", historial)
        else: 
            print("No puedes volver, historial vacío.")
    
    elif opcion == 4:
        # Verifica si el historial está vacío
        if len(historial) == 0:
            print("El historial está vacío.")
        else:
            print("Páginas restantes:", historial)
    
    elif opcion == 5:
        print("Saliendo del programa...")
        break  # Salir del bucle while
    

