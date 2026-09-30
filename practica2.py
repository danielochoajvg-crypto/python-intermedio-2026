# Práctica 2

'''
Escribe un programa que intente dividir dos números. Si el segundo número es cero,
captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.
'''

try:
    a = 5 / 0
    print (a)
except ZeroDivisionError as e:
    print (f"Ha ocurrido un error {e}")

'''
Escribe un programa que intente sumar un número y una cadena. Si se produce un error
de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.
'''

try:
    a = 5 + "hola"
    print (a)
except TypeError as e:
    print (f"Ha ocurrido un error {e}")

'''
Escribe un programa que intente acceder a una clave que no existe en un
diccionario. Si se produce una excepción KeyError, captura la excepción y muestra
'''
alumno = {
    "alumno": "Casimiro",
    "edad": 33,
    "curso": "Python"
}
try:
    print(alumno["nombre"])
except KeyError as e:
    print (f"Ha ocurrido un error {e}")

'''
Escribe
un programa que
intente abrir un archivo que no existe. Si se produce una excepción
FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin
embargo, también intenta crear el archivo si no existe.
'''

try:
    with open("archivo.txt", "r") as archivo:
        contenido = archivo.read()
    print(contenido)
except FileNotFoundError as e:
    print (f"Ha ocurrido un error {e}")
    with open("archivo.txt", "x") as archivo:
        archivo.write("Este es un archivo nuevo.")


'''
Escribe un programa que intente dividir dos números. Si el segundo número es cero,
captura la excepción ZeroDivisionError. Si el primer número es un número no válido,
captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.
'''
def dividir(a,b):
    return a / b

nume = 0

try:
    n1 = float ("zaraza")
    n2 = float (0)
    nume = dividir (n1,n2)

except ZeroDivisionError:
    print ("Ha ocurrido un error al dividir por cero")
except ValueError:
    print ("Ha ocurrido un error de número no válido")
else:
    print ("continuo como si nada")



