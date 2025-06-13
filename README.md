# 📊 Proyecto: Operaciones con DNIs y Años de Nacimiento

## 📝 Descripción

Este proyecto integrador en Python, realizado en la materia Matemática de la Tecnicatura Universitaria en Programación - UTN, realiza diversas operaciones matemáticas y lógicas aplicadas a conjuntos de dígitos únicos extraídos de DNIs y a años de nacimiento de los integrantes del grupo. El programa integra conceptos de teoría de conjuntos, lógica y programación para analizar y procesar datos reales o ficticios.

---

## 🛠️ Estructura del Programa

El programa principal (`main`) presenta un menú interactivo con tres opciones:

1. **🔢 Operaciones con DNI**  
   Permite ingresar varios DNIs, generar conjuntos de dígitos únicos, y calcular operaciones entre conjuntos (unión, intersección, diferencia y diferencia simétrica). Además, cuenta la frecuencia y suma de los dígitos en cada DNI, detecta dígitos compartidos entre todos los DNIs y verifica la diversidad numérica en los conjuntos.

2. **📅 Operaciones con años de nacimiento**  
   Permite ingresar los años de nacimiento de los integrantes, contar cuántos nacieron en años pares e impares, identificar si todos pertenecen a la "Generación Z" (nacidos después del 2000), detectar años bisiestos y calcular el producto cartesiano entre los conjuntos de años y edades actuales.

3. **🚪 Salir**  
   Termina la ejecución del programa.

---

## ⚙️ Descripción de Funciones

### Funciones principales del módulo de años (`operacionesConAños`):

- `bis(año)`: Determina si un año es bisiesto según las reglas estándar.  
- `operacionesConAños()`: Solicita años de nacimiento, realiza conteos de pares/impares, verifica condiciones especiales (Grupo Z, año bisiesto) y calcula el producto cartesiano de años y edades.

### Funciones principales del módulo de DNIs (`operacionesConDNI`):

- `definir_dnis()`: Solicita al usuario ingresar múltiples DNIs y valida la entrada.  
- `definir_conjuntos()`: Genera conjuntos de dígitos únicos para cada DNI ingresado.  
- `operacion_conjuntos(conjuntos)`: Calcula unión, intersección, diferencia y diferencia simétrica entre los conjuntos.  
- `frecuencia_digitos(dni)`: Cuenta y muestra la frecuencia de cada dígito en un DNI.  
- `suma_digitos(dni)`: Calcula y muestra la suma de los dígitos de un DNI.  
- `digito_en_todos_los_dnis(dnis)`: Identifica dígitos que aparecen en todos los DNIs.  
- `verificar_diversidad_numerica()`: Muestra cuáles conjuntos tienen alta diversidad (más de 6 elementos).  
- `menu()`: Controla el menú específico para operaciones con DNIs, permitiendo al usuario seleccionar diferentes funcionalidades.

---

## 🚀 Cómo ejecutar el programa

1. Ejecutar el archivo principal que contiene la función `main()`.  
2. Seleccionar una opción del menú para realizar operaciones con DNIs o con años de nacimiento.  
3. Seguir las instrucciones en pantalla para ingresar datos y obtener resultados.

---

## 👨‍💻 Desarrolladores

- Shai Kohn 
- Lautaro Lucero 
- Gabriela Machin

---

## 🎥 Enlace al video

La presentación del proyecto está disponible en el siguiente link:  
[🔗 Video de Presentación](https://youtu.be/1MG3uIPOkFQ)  

---

¡Gracias por usar nuestro programa! 🎉
