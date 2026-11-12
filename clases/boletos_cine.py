

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
    def __init__(self, cliente, precio_base, funcion):
        super().__init__(cliente, funcion)
        self.precio_base = precio_base

    def calcular_precio(self):
        return self.precio_base * 0.7


class boleto_cortesia(boleto):
    def __init__(self, cliente, funcion):
        super().__init__(cliente, funcion)
        self.precio_base = 0
    
    def calcular_precio(self):
        return self.precio_base
        

