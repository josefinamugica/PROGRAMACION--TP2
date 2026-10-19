
import csv
import re
from datetime import datetime
from dominio import BalanceEstacion

COLUMNAS_OBLIGATORIAS = [
    "id_recorrido",
    "fecha_origen_recorrido",
    "fecha_destino_recorrido",
    "id_estacion_origen",
    "id_estacion_destino",
    "nombre_estacion_origen",
    "nombre_estacion_destino"
]


def validar_esquema(viajes):
    if not viajes:
        raise ValueError("El archivo no contiene viajes.")

    for numero, viaje in enumerate(viajes, start=1):
        if not isinstance(viaje, dict):
            raise ValueError(
                f"El registro {numero} no tiene una estructura válida."
            )

        faltantes = [
            columna for columna in COLUMNAS_OBLIGATORIAS
            if columna not in viaje
        ]

        if faltantes:
            raise ValueError(
                f"Al registro {numero} le faltan columnas: "
                + ", ".join(faltantes)
            )

    return True





def validar_recorridos(viajes):
    viajes_validos = []
    viajes_rechazados = []
    identificadores = set()

    patron_fecha = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"

    for viaje in viajes:
        motivo = None
        valor_id = viaje["id_recorrido"]
        identificador = "" if valor_id is None else str(valor_id).strip()

        if not identificador:
            motivo = "Identificador de viaje vacío"

        elif identificador in identificadores:
            motivo = "Viaje duplicado"

        else:
            if any(
                    viaje[campo] is None or not str(viaje[campo]).strip()
                    for campo in [
                                     "id_estacion_origen",
                                     "id_estacion_destino",
                                      "nombre_estacion_origen",
                                      "nombre_estacion_destino"
                     ]
            ):

                     motivo = "Estación de origen o destino incompleta"

            elif not all(
                str(viaje[campo]).strip().isdigit()
                for campo in ["id_estacion_origen", "id_estacion_destino"]
            ):
                motivo = "Identificador de estación inválido"

            else:
                try:
                    inicio = str(viaje["fecha_origen_recorrido"]).strip()
                    fin = str(viaje["fecha_destino_recorrido"]).strip()

                    if not re.fullmatch(patron_fecha, inicio) or not re.fullmatch(patron_fecha, fin):
                        raise ValueError("Formato de fecha incorrecto")

                    fecha_inicio = datetime.strptime(inicio, "%Y-%m-%d %H:%M:%S")
                    fecha_fin = datetime.strptime(fin, "%Y-%m-%d %H:%M:%S")

                    if fecha_fin < fecha_inicio:
                        motivo = "La finalización es anterior al inicio"

                except (ValueError, TypeError):
                    motivo = "Fecha inválida o incorrecta"

        if motivo:
            viajes_rechazados.append({
                        "viaje": viaje,
                        "motivo": motivo
             })
        else:
            viajes_validos.append(viaje)
            identificadores.add(identificador)

    return viajes_validos, viajes_rechazados


def guardar_rechazos(viajes_rechazados, ruta_salida):
    columnas = COLUMNAS_OBLIGATORIAS + ["motivo_rechazo"]

    with open(ruta_salida, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()

        for rechazo in viajes_rechazados:
            fila = rechazo["viaje"].copy()
            fila["motivo_rechazo"] = rechazo["motivo"]
            escritor.writerow(fila)

def seleccionar_periodo(viajes_validos, fecha_desde, fecha_hasta):
    inicio_periodo = datetime.strptime(fecha_desde, "%Y-%m-%d %H:%M:%S")
    fin_periodo = datetime.strptime(fecha_hasta, "%Y-%m-%d %H:%M:%S")

    if inicio_periodo > fin_periodo:
        raise ValueError(
            "La fecha inicial no puede ser posterior a la fecha final."
        )

    viajes_seleccionados = []

    for viaje in viajes_validos:
        inicio_viaje = datetime.strptime(
            viaje["fecha_origen_recorrido"],
            "%Y-%m-%d %H:%M:%S"
        )

        if inicio_periodo <= inicio_viaje <= fin_periodo:
            viajes_seleccionados.append(viaje)

    return viajes_seleccionados


def registrar_movimientos(viajes_seleccionados):
    movimientos = {}

    for viaje in viajes_seleccionados:
        origen = viaje["id_estacion_origen"]
        destino = viaje["id_estacion_destino"]

        nombre_origen = viaje["nombre_estacion_origen"]
        nombre_destino = viaje["nombre_estacion_destino"]

        if origen not in movimientos:
            movimientos[origen] = BalanceEstacion(origen, nombre_origen)

        if destino not in movimientos:
            movimientos[destino] = BalanceEstacion(destino, nombre_destino)

        movimientos[origen].registrar_salida()
        movimientos[destino].registrar_llegada()

    return movimientos



def generar_balance(movimientos):
    reporte = []

    for id_estacion, estacion in movimientos.items():
        reporte.append({
            "id_estacion": id_estacion,
            "nombre_estacion": estacion.nombre,
            "salidas": estacion.salidas,
            "llegadas": estacion.llegadas,
            "balance_neto": estacion.calcular_balance()
        })

    return reporte

def exportar_reporte(reporte, ruta_salida):
    columnas = [
        "id_estacion",
        "nombre_estacion",
        "salidas",
        "llegadas",
        "balance_neto"
    ]

    with open(ruta_salida, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()
        escritor.writerows(reporte)
