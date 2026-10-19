
import csv
import json
from abc import ABC, abstractmethod


class FuenteDatos(ABC):
    @abstractmethod
    def cargar(self, ruta):
        pass


class FuenteCSV(FuenteDatos):
    def cargar(self, ruta):
        with open(ruta, "r", encoding="utf-8-sig", newline="") as archivo:
            lector = csv.DictReader(archivo)
            return list(lector)


class FuenteJSON(FuenteDatos):
    def cargar(self, ruta):
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        if not isinstance(datos, list) or not all(
            isinstance(viaje, dict) for viaje in datos
        ):
            raise ValueError("El JSON debe contener una lista de viajes.")

        return datos


        