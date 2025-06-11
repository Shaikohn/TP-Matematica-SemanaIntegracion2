dnis = ["45539208", "37048164", "47248462"]
conjuntos = []

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
    print("Unión:", union)
    print("Intersección:", interseccion)
    print("Diferencia:", diferencia)
    print("Diferencia simétrica:", diferencia_simetrica)

def definir_conjuntos(dnis):
    for dni in dnis:
        conjunto = set()
        for i in range(0, 10):
            if str(i) in dni:
                conjunto.add(i)
        conjuntos.append(conjunto)
    print(conjuntos)
    for conjunto in conjuntos:
        if len(conjunto) > 6:
            print(f"El conjunto {conjunto} diversidad numérica alta")
    operacion_conjuntos(conjuntos)

def frecuencia_digitos(dni):
    frecuencia = {}
    for digito in dni:
        if digito.isdigit():
            if digito in frecuencia:
                frecuencia[digito] += 1
            else:
                frecuencia[digito] = 1
    print(f"Frecuencia de dígitos en {dni}: {frecuencia}")

def suma_digitos(dni):
    suma = 0
    for digito in dni:
        if digito.isdigit():
            suma += int(digito)
    print(f"Suma de dígitos en {dni}: {suma}")

def digito_en_todos_los_dnis():
    for i in range(0, 10):
        if all(str(i) in dni for dni in dnis):
            print(f"El dígito {i} es un dígito compartido")

definir_conjuntos(dnis)
frecuencia_digitos("45539208")
suma_digitos("45539208")
digito_en_todos_los_dnis()
