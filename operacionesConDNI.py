dnisDePrueba = ["45539208", "37048164", "47248462"]
conjuntos = []
dnis = []

def definir_dnis():
    cantidadDeDnis = int(input("Ingresa el total de DNIs a calcular: "))
    while cantidadDeDnis <= 1:
        print("El número de DNIs debe ser mayor a 1.")
        cantidadDeDnis = int(input("Ingresa el total de DNIs a calcular: "))
    contador = 1
    while cantidadDeDnis > 0:
        dni = input(f"Ingresa el DNI numero {contador}: ")
        if not dni.isdigit():
            print("El DNI debe contener solo dígitos.")
            continue
        dnis.append(dni)
        contador += 1
        cantidadDeDnis -= 1
    definir_conjuntos()

def operacion_conjuntos(conjuntos):
    union = set()
    interseccion = set()
    diferencia = set()
    diferencia_simetrica = set()
    for conjunto in conjuntos:
        union = union.union(conjunto)
        if not interseccion:
            interseccion = conjunto
        else:
            interseccion = interseccion.intersection(conjunto)
        if not diferencia:
            diferencia = conjunto
        else:
            diferencia = diferencia.difference(conjunto)
        if not diferencia_simetrica:
            diferencia_simetrica = conjunto
        else:
            diferencia_simetrica = diferencia_simetrica.symmetric_difference(conjunto)
    print("------ Operaciones con conjuntos ---")
    print("Unión:", union)
    print("Intersección:", interseccion)
    print("Diferencia:", diferencia)
    print("Diferencia simétrica:", diferencia_simetrica)

def definir_conjuntos():
    for dni in dnis:
        conjunto = set()
        for i in range(0, 10):
            if str(i) in dni:
                conjunto.add(i)
        conjuntos.append(conjunto)
    print("------ Conjuntos ---")
    print(conjuntos)
    operacion_conjuntos(conjuntos)

def frecuencia_digitos(dni):
    frecuencia = {}
    for digito in dni:
        if digito.isdigit():
            if digito in frecuencia:
                frecuencia[digito] += 1
            else:
                frecuencia[digito] = 1
    print(f"Frecuencia de dígitos en el DNI {dni}: {frecuencia}")

def suma_digitos(dni):
    suma = 0
    for digito in dni:
        if digito.isdigit():
            suma += int(digito)
    print(f"Suma de dígitos en el DNI {dni}: {suma}")

def digito_en_todos_los_dnis(dnis):
    for i in range(0, 10):
        if all(str(i) in dni for dni in dnis):
            print(f"El dígito {i} es un dígito compartido en todos los DNIs.")

def verificar_diversidad_numerica():
        for conjunto in conjuntos:
            if len(conjunto) > 6:
                print(f"El conjunto {conjunto} tiene diversidad numérica alta")

def menu():
    definir_dnis()
    print("------ Funciones adicionales ---")
    print("1. Verificar dígito en todos los DNIs")
    print("2. Calcular frecuencia de dígitos")
    print("3. Calcular suma de dígitos")
    print("4. Verificar diversidad numérica")
    print("5. Realizar todas las funciones adicionales")
    print("6. Salir")
    opcion = int(input("Selecciona una opción: "))
    if opcion == 1:
        digito_en_todos_los_dnis(dnis)
    elif opcion == 2:
        for dni in dnis:
            frecuencia_digitos(dni)
    elif opcion == 3:
        for dni in dnis:
            suma_digitos(dni)
    elif opcion == 4:
        verificar_diversidad_numerica()
    elif opcion == 5:
        digito_en_todos_los_dnis(dnis)
        for dni in dnis:
            print("---------")
            frecuencia_digitos(dni)
            suma_digitos(dni)
        print("---------")
        verificar_diversidad_numerica()
    elif opcion == 6:
        print("Saliendo del programa.")
        return
    else:
        print("Opción no válida.")