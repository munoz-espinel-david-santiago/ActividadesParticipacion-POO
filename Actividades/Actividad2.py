#PUNTO1
class Vehiculo:
    def __init__(self, velocidad_maxima, kilometraje):

        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

    def __str__(self):

        return f"Vehículo con velocidad máxima de {self.velocidad_maxima} km/h y kilometraje de {self.kilometraje} km"

mi_vehiculo = Vehiculo(200, 50000)
print(mi_vehiculo)     


#PUNTO2
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    

#PUNTO3:
#3.1- Un método mostrar que imprima por consola las coordenadas del punto
#3.2 Un método mover que cambie las coordenadas del punto
#3.3 Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.

    def mostrar(self):
        print(f"Las coordenadas del punto son: ({self.x}, {self.y})")

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def calcular_distancia(self, otro_punto):
        dx = self.x - otro_punto.x
        dy = self.y - otro_punto.y
        return (dx ** 2 + dy ** 2) ** 0.5

punto1 = Punto(1, 2)
punto2 = Punto(4, 6)

punto1.mostrar()

punto1.mover(2, 3)
punto1.mostrar()

distancia = punto1.calcular_distancia(punto2)
print(f"La distancia entre los puntos es {distancia:.2f}")

#PUNTO4:
# 4.1 Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que definen sus esquinas
# 4.2Agregue métodos a la clase Rectángulo para calcular su  perímetro,
# 4.3Calcular su área e indicar si el rectángulo es un cuadrado.

class Rectangulo:
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2

    def calcular_perimetro(self):
        ancho = abs(self.punto1.x - self.punto2.x)
        alto = abs(self.punto1.y - self.punto2.y)
        return 2 * (ancho + alto)

    def calcular_area(self):
        ancho = abs(self.punto1.x - self.punto2.x)
        alto = abs(self.punto1.y - self.punto2.y)
        return ancho * alto

    def es_cuadrado(self):
        ancho = abs(self.punto1.x - self.punto2.x)
        alto = abs(self.punto1.y - self.punto2.y)
        return ancho == alto
    
punto1 = Punto(1, 1)
punto2 = Punto(5, 5)

rectangulo = Rectangulo(punto1, punto2)
print(f"El perímetro del rectángulo es {rectangulo.calcular_perimetro():.2f}")
print(f"El área del rectángulo es {rectangulo.calcular_area():.2f}")
print(f"El rectángulo es un cuadrado: {rectangulo.es_cuadrado()}")


#PUNTO5
class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def area(self):
        pi = 3.141592653589793
        return pi * self.radio ** 2

    def perimetro(self):
        pi = 3.141592653589793
        return 2 * pi * self.radio

    def pertenece(self, punto):
        dx = punto[0] - self.centro[0]
        dy = punto[1] - self.centro[1]
        distancia_cuadrada = dx ** 2 + dy ** 2
        return distancia_cuadrada <= self.radio ** 2
    
#PUNTO6
class Carta:
    CORAZONES = "Corazones"
    DIAMANTES = "Diamantes"
    TREBOLES = "Tréboles"
    PICAS = "Picas"

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

#PUNTO7
class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance


#PUNTO8
    def depositar(self, valor):
        if valor > 0:
            self.balance += valor
            print(f"Depósito de {valor} realizado. Nuevo balance: {self.balance}")
        else:
            print("El valor a depositar debe ser mayor que cero.")


#PUNTO9
    def retirar(self, valor):
        if valor > 0:
            if valor <= self.balance:
                self.balance -= valor
                print(f"Retiro de {valor} realizado. Nuevo balance: {self.balance}")
            else:
                print("Fondos insuficientes para el retiro.")
        else:
            print("El valor a retirar debe ser mayor que cero.")

#PUNTO10
    def aplicar_cuota_manejo(self):
        porcentaje = 0.02
        cuota = self.balance * porcentaje
        self.balance -= cuota
        print(f"Cuota de manejo de {cuota} .El nuevo balance es: {self.balance}")


#PUNTO11
def mostrar_detalles(self):
        print(f"Su número de cuenta es: {self.numero_cuenta}")
        print(f"Propietarios: {', '.join(self.propietarios)}")
        print(f"Balance: {self.balance}")