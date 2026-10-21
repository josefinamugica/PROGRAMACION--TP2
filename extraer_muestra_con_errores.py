import csv
import re
from datetime import datetime
from pathlib import Path
import sys

if len(sys.argv) != 2:
    print("Uso: py extraer_muestra_con_errores.py ruta_del_csv_original")
    sys.exit(1)

RUTA_ORIGINAL = Path(sys.argv[1])

RUTA_ORIGINAL = Path(sys.argv[1])

RUTA_SALIDA = Path(__file__).resolve().parent / "data" / "viajes_ecobici.csv"
COLUMNAS = [
    "id_recorrido",
    "fecha_origen_recorrido",
    "fecha_destino_recorrido",
    "id_estacion_origen",
    "id_estacion_destino",
    "nombre_estacion_origen",
    "nombre_estacion_destino"
]

PATRON_FECHA = (
    r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
)


def fecha_invalida(viaje):
    try:
        inicio = viaje["fecha_origen_recorrido"]
        fin = viaje["fecha_destino_recorrido"]

        if not re.fullmatch(PATRON_FECHA, inicio or ""):
            return True

        if not re.fullmatch(PATRON_FECHA, fin or ""):
            return True

        fecha_inicio = datetime.strptime(
            inicio, "%Y-%m-%d %H:%M:%S"
        )
        fecha_fin = datetime.strptime(
            fin, "%Y-%m-%d %H:%M:%S"
        )

        return fecha_fin < fecha_inicio

    except (ValueError, TypeError):
        return True


viajes_validos = []
viajes_invalidos = []
identificadores = set()

with RUTA_ORIGINAL.open(
    "r", encoding="utf-8-sig", newline=""
) as archivo:

    lector = csv.DictReader(archivo)

    for viaje in lector:
        id_viaje = (viaje["id_recorrido"] or "").strip()

        estaciones_correctas = all(
            (viaje[campo] or "").strip()
            for campo in [
                "id_estacion_origen",
                "id_estacion_destino",
                "nombre_estacion_origen",
                "nombre_estacion_destino"
            ]
        )

        estaciones_correctas = (
            estaciones_correctas
            and all(
                (viaje[campo] or "").strip().isdigit()
                for campo in [
                    "id_estacion_origen",
                    "id_estacion_destino"
                ]
            )
        )

        duplicado = id_viaje in identificadores

        if id_viaje and not duplicado:
            identificadores.add(id_viaje)

        es_invalido = (
            not id_viaje
            or duplicado
            or not estaciones_correctas
            or fecha_invalida(viaje)
        )

        seleccionado = {
            columna: viaje[columna]
            for columna in COLUMNAS
        }

        if es_invalido and len(viajes_invalidos) < 20:
            viajes_invalidos.append(seleccionado)

        elif not es_invalido and len(viajes_validos) < 180:
            viajes_validos.append(seleccionado)

        if len(viajes_validos) == 180 and len(viajes_invalidos) == 20:
            break


muestra = viajes_validos + viajes_invalidos

RUTA_SALIDA.parent.mkdir(exist_ok=True)

with RUTA_SALIDA.open(
    "w", encoding="utf-8", newline=""
) as archivo:

    escritor = csv.DictWriter(
        archivo, fieldnames=COLUMNAS
    )
    escritor.writeheader()
    escritor.writerows(muestra)


print("=== MUESTRA DE ECOBICI ===")
print("Viajes válidos seleccionados:", len(viajes_validos))
print("Viajes inválidos seleccionados:", len(viajes_invalidos))
print("Total de registros:", len(muestra))
print("Archivo generado:", RUTA_SALIDA)
