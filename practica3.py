"""
Práctica
1) Calcular el mayor de dos números ingresados por teclado usando un operador
ternario.
2) Buscar una palabra en una lista ingresada por teclado usando args y un operador
ternario.
3) Determinar si un número es par o impar.
4) Calcular el promedio de una lista de números usando args y un operador ternario.
5) Imprimir un mensaje de error si no se pasan suficientes argumentos
"""

# 1
print("\n1) Calcular el mayor de dos números")
n = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))

resultado = (
    "El primer número es mayor."
    if n > n2
    else "El segundo número es mayor."
    if n2 > n
    else "Los dos números son iguales."
)
print(resultado)


# 2

print("\n2) Buscar palabra")

def buscar(palabra, *args):
    return "Encontrada" if palabra in args else "No encontrada"

palabras = []
continuar = "s"

while continuar == "s":
    fruta = input("Ingrese una fruta: ")
    palabras.append(fruta)
    continuar = input("¿Desea ingresar otra fruta? (s/n): ")

busqueda = input("Ingrese la palabra que desea buscar: ")

print(buscar(busqueda, *palabras))

# 3
print("\n3) Determinar número par o impar")
numero = int(input("Ingrese un número entero: "))

print("El número es par." if numero % 2 == 0 else "El número es impar.")

# 4
print("\n4) Calcular el promedio de una lista de números...")

def promedio(*args):
    return sum(args) / len(args) if len(args) > 0 else None

numeros = []
continuar = "s"

while continuar == "s":
    try:
        numero = float(input("Ingrese un número: "))
        numeros.append(numero)
    except ValueError:
        print("Error: ingrese un número válido.")

    continuar = input("¿Desea ingresar otro número? (s/n): ")

if len(numeros) > 0:
    resultado = promedio(*numeros)
    print("El promedio es:", resultado)
else:
    print("Error: debe ingresar al menos un número.")

# 5
print("\n5) Imprimir un mensaje de error si no se pasan suficientes argumentos")

def mostrar_datos(*args):
    if len(args) < 2:
        print("Error: faltan argumentos. Debe indicar un nombre y una edad.")
    else:
        nombre, edad = args[0], args[1]
        print(f"Nombre: {nombre}; edad: {edad}")

mostrar_datos("Pepe")   # devuelve error porque le falta un argumento
