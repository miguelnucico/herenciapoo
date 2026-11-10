
class estancia (object):
    def __init__(self, placas, hora):
        self.placas = placas
        self.hora = hora

    def calcular_precio(self):
        return self.hora * 20

    def ticket(self):
        return f"{self.placas} - Tiempo: {self.hora}: ${self.calcular_precio():,.2f}"

class pension(estancia):
    def __init__(self, placas, dia):
        self.dia = dia
        super().__init__(placas, 0)

    def calcular_precio(self):
        return self.dia * 250

class noche(estancia):
    def __init__(self, placas):
        super().__init__(placas, 12)

    def calcular_precio(self):
        return super().calcular_precio() + 50
