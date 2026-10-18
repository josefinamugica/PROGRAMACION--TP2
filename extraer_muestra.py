
import csv
import sys
from pathlib import Path

if len(sys.argv) != 2:
    print("Uso: py extraer_muestra.py ruta_del_archivo_original.csv")
    sys.exit(1)

archivo_original = Path(sys.argv[1])
archivo_muestra = Path(__file__).resolve().parent / "data" / "viajes_ecobici.csv"

columnas = [
    "id_recorrido",
    "fecha_origen_recorrido",
    "fecha_destino_recorrido",
    "id_estacion_origen",
    "id_estacion_destino",
    "nombre_estacion_origen",
    "nombre_estacion_destino"
]

with open(archivo_original, "r", encoding="utf-8-sig", newline="") as entrada:
    lector = csv.DictReader(entrada)

    with open(archivo_muestra, "w", encoding="utf-8", newline="") as salida:
        escritor = csv.DictWriter(salida, fieldnames=columnas)
        escritor.writeheader()

        for numero, viaje in enumerate(lector):
            if numero >= 100:
                break
            escritor.writerow({columna: viaje[columna] for columna in columnas})

print("Muestra de 100 viajes guardada correctamente.")
