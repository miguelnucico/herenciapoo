#Tiene cliente: función y precio base de $90. Sabe calcular su precio y generar su ticket con el formato Cliente - Función: $precio. 
#BoletoEstudiante:Cuesta lo mismo que un boleto normal, con un 30 % de descuento. 
#BoletoCortesia:Siempre cuesta $0.

class boleto(object):
    def __init__(self, cliente, funcion):
        self.cliente = cliente
        self.funcion = funcion
        self.precio_base = 90

    def calcular_precio(self):
        return self.precio_base

    def ticket(self):
        return f"{self.cliente} - {self.funcion}: ${self.calcular_precio():,.2f}"


class boleto_estudiante(boleto):
    def calcular_precio(self):
        return self.precio_base * 0.7


class boleto_cortesia(boleto):
    def calcular_precio(self):
        return 0
