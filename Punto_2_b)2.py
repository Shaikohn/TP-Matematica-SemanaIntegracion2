##Parte 2 – Desarrollo del Programa en Python  // Kohn, Lucero, Machin
##B. Operaciones con años de nacimiento

def bis(año):
    if (año % 4 == 0) and (año % 100 != 0) or (año % 400 == 0):
        return 1
    else:
        return 0

cant = int(input("Ingrese la cantidad de integrantes de su grupo: "))
par = impar = edad = 0
Z = True
B = False

años = []
edades = []
for i in range(cant):
    año = int(input("Ingrese el año de nacimiento: "))
    años.append(año)
    if año % 2 == 0:
        par += 1
    else:
        impar += 1
    if año < 2000:
        Z = False
    if bis(año):
        B = True
    edad = 2025 - año
    edades.append(edad)

print(f"Hay {par} integrantes nacidos en año par y {impar} integrantes nacidos en año impar.")
if Z:
    print("Grupo Z")
if B:
    print("Tenemos un año especial")

producto_cartesiano = [(a, e) for a in años for e in edades]
print("\nProducto cartesiano:")
for par in producto_cartesiano:
    print(f"    {par}")