
import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from fuentes import FuenteCSV

from pipeline import (
    validar_recorridos,
    registrar_movimientos,
    generar_balance
)


class TestEcobici(unittest.TestCase):
#. un caso normal;
    def test_viaje_normal(self):
        viaje = {
            "id_recorrido": "1",
            "fecha_origen_recorrido": "2024-01-23 10:00:00",
            "fecha_destino_recorrido": "2024-01-23 10:15:00",
            "id_estacion_origen": "100",
            "id_estacion_destino": "200",
            "nombre_estacion_origen": "Estación A",
            "nombre_estacion_destino": "Estación B"
        }

        validos, rechazados = validar_recorridos([viaje])

        self.assertEqual(len(validos), 1)
        self.assertEqual(len(rechazados), 0)

        movimientos = registrar_movimientos(validos)
        reporte = generar_balance(movimientos)

        estaciones = {
            estacion["id_estacion"]: estacion
            for estacion in reporte
        }

        self.assertEqual(estaciones["100"]["salidas"], 1)
        self.assertEqual(estaciones["100"]["llegadas"], 0)
        self.assertEqual(estaciones["100"]["balance_neto"], -1)

        self.assertEqual(estaciones["200"]["salidas"], 0)
        self.assertEqual(estaciones["200"]["llegadas"], 1)
        self.assertEqual(estaciones["200"]["balance_neto"], 1)

# una entrada inválida o un caso límite
    def test_fecha_invalida(self):
        viaje = {
            "id_recorrido": "2",
            "fecha_origen_recorrido": "2024-02-30 10:00:00",
            "fecha_destino_recorrido": "2024-02-30 10:15:00",
            "id_estacion_origen": "100",
            "id_estacion_destino": "200",
            "nombre_estacion_origen": "Estación A",
            "nombre_estacion_destino": "Estación B"
        }

        validos, rechazados = validar_recorridos([viaje])

        self.assertEqual(len(validos), 0)
        self.assertEqual(len(rechazados), 1)
        self.assertEqual(
            rechazados[0]["motivo"],
            "Fecha inválida o incorrecta"
        )

# una propiedad relevante del resultado 
    def test_conservacion_movimientos(self):
        viajes = [
            {
                "id_recorrido": str(i),
                "fecha_origen_recorrido": "2024-01-23 10:00:00",
                "fecha_destino_recorrido": "2024-01-23 10:15:00",
                "id_estacion_origen": origen,
                "id_estacion_destino": destino,
                "nombre_estacion_origen": f"Estación {origen}",
                "nombre_estacion_destino": f"Estación {destino}"
            }
            for i, (origen, destino) in enumerate(
                [("100", "200"), ("100", "300"), ("200", "100")],
                 start=1
            )
        ]
    
        validos, rechazados = validar_recorridos(viajes)
        movimientos = registrar_movimientos(validos)
        reporte = generar_balance(movimientos)
    
        total_salidas = sum(e["salidas"] for e in reporte)
        total_llegadas = sum(e["llegadas"] for e in reporte)
        balance_total = sum(e["balance_neto"] for e in reporte)
    
        self.assertEqual(len(validos), 3)
        self.assertEqual(len(rechazados), 0)
        self.assertEqual(total_salidas, 3)
        self.assertEqual(total_llegadas, 3)
        self.assertEqual(balance_total, 0)

#2 ADICIONALES:
    
    def test_viaje_duplicado(self):
        viaje = {
            "id_recorrido": "10",
            "fecha_origen_recorrido": "2024-01-23 10:00:00",
            "fecha_destino_recorrido": "2024-01-23 10:15:00",
            "id_estacion_origen": "100",
            "id_estacion_destino": "200",
            "nombre_estacion_origen": "Estación A",
            "nombre_estacion_destino": "Estación B"
        }

        validos, rechazados = validar_recorridos([viaje, viaje.copy()])

        self.assertEqual(len(validos), 1)
        self.assertEqual(len(rechazados), 1)
        self.assertEqual(
            rechazados[0]["motivo"],
            "Viaje duplicado"
        )
    
    def test_estacion_faltante(self):
        viaje = {
            "id_recorrido": "20",
            "fecha_origen_recorrido": "2024-01-23 10:00:00",
            "fecha_destino_recorrido": "2024-01-23 10:15:00",
            "id_estacion_origen": "100",
            "id_estacion_destino": "200",
            "nombre_estacion_origen": "Estación A",
            "nombre_estacion_destino": None
        }

        validos, rechazados = validar_recorridos([viaje])

        self.assertEqual(len(validos), 0)
        self.assertEqual(len(rechazados), 1)
        self.assertEqual(
            rechazados[0]["motivo"],
            "Estación de origen o destino incompleta"
        )

## Una comprobación de que el programa no oculta fallas de lectura: archivo CSV inexistente
    def test_archivo_inexistente(self):
        ruta = (
            Path(__file__).resolve().parent
            / "archivo_inexistente_ecobici.csv"
        )

        fuente = FuenteCSV()

        with self.assertRaises(FileNotFoundError):
            fuente.cargar(ruta)

 

if __name__ == "__main__":
    unittest.main()
