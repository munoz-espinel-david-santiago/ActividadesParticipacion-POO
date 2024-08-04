#PUNTO!
nombre = input("Por favor, ingresa tu nombre: ")
edad = int(input("Por favor, ingresa tu edad: "))

print(f"Hola {nombre}, tienes {edad} años.")


#PUNTO2
pi = 3.141592653589793
radio = float(input("Ingresa el radio del círculo: "))
area = pi * radio ** 2

print(f"El área del círculo con radio {radio} es {area:.2f}")


#PUNTO3
import random
cantidad = int(input("Ingresa la cantidad de números aleatorios que quiere generar: "))
lista_aleatoria = [random.randint(0, 10000) for x in range(cantidad)]

print("Lista de números aleatorios generada:", lista_aleatoria)


#PUNTO4
numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")


#PUNTO5
fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit} grados Fahrenheit son {celsius:.2f} grados Celsius.")


#PUNTO6
numeros = [1, 24, 53, 44, 53,26]
suma = sum(numeros)
print("La suma de los números en la lista es:",suma)


#PUNTO7
numeros = [34, 78, 12, 89, 23, 56, 7]
mayor = max(numeros)
menor = min(numeros)
print("El número más grande en la lista es:",mayor)
print(f"El número más pequeño en la lista es: {menor}")

#PUNTO8
mi_lista = [1, 2, 3, 4, 5]
mi_lista = mi_lista[::-1]
print("Lista invertida:", mi_lista)


#PUNTO9
matriz = []
contador = 1
for i in range(filas):
    fila = []
    for j in range(columnas): 
        fila.append(contador)
        contador = contador + 1
    matriz.append(fila)
for fila in matriz:
    print(fila)


#PUNTO10
numero = int(input("Ingresa un número entero positivo: "))
factorial = 1
for i in range(1, numero + 1):
    factorial *= i

print(f"El factorial de {numero} es: {factorial}")


#PUNTO11
pares = []

for numero in range(1, 101):
    if numero % 2 == 0:
        pares.append(numero)

print(pares)


#PUNTO12
for numero in range(1, 11):
    print(numero)


#PUNTO13

num1=float(input("ingrese primer un numero"))
num2=float(input("ingrese segundo un numero"))
sum= num1+num2
res=num1-num2
mul= num1*num2
div=num1/num2

print(f"la suma de sus numeros es {sum},la multiplicacion de sus numeros es{mul},la resta de sus numeros es{res},la division de sus numeros es{div}")


#PUNTO14
numeros = [11, 22, 33, 40, 50]
prom=sum(numeros)/len(numeros)
print(prom)


#PUNTO15
texto = input("Ingresa una cadena de texto: ")
texto_limpio = texto.replace(" ", "").lower()
if texto_limpio == texto_limpio[::-1]:
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")

