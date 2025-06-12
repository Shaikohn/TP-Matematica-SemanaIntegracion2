import operacionesConDNI, operacionesConAños

def main():
    print("Bienvenido al programa de operaciones con DNI y años de nacimiento.")
    print("Por favor, elija una de las siguientes opciones:")
    print("1. Operaciones con DNI")
    print("2. Operaciones con años de nacimiento")
    print("3. Salir")
    opcion = int(input("Selecciona una opción: "))
    if opcion == 1:
        operacionesConDNI.menu()
    elif opcion == 2:
        operacionesConAños.operacionesConAños()
    elif opcion == 3:
        print("Saliendo del programa.")
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
if __name__ == "__main__":
    main()