
class BalanceEstacion:
    def __init__(self, id_estacion, nombre):
        self.id_estacion = id_estacion
        self.nombre = nombre
        self.salidas = 0
        self.llegadas = 0

    def registrar_salida(self):
        self.salidas += 1

    def registrar_llegada(self):
        self.llegadas += 1

    def calcular_balance(self):
        return self.llegadas - self.salidas
