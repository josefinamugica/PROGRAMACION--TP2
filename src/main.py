
from pathlib import Path
from fuentes import FuenteCSV, FuenteJSON
from pipeline import (
    validar_esquema,
    validar_recorridos,
    guardar_rechazos,
    seleccionar_periodo,
    registrar_movimientos,
    generar_balance,
    exportar_reporte
)
import json

def main():
    print("=== REPORTE DE MOVIMIENTOS DE ECOBICI ===")

    formato = input("Elegí el formato de los datos (csv/json): ").strip().lower()

    carpeta_proyecto = Path(__file__).resolve().parent.parent

    if formato == "csv":
        fuente = FuenteCSV()
        ruta = carpeta_proyecto / "data" / "viajes_ecobici.csv"

    elif formato == "json":
        fuente = FuenteJSON()
        ruta = carpeta_proyecto / "data" / "viajes_ecobici.json"

    else:
        print("Error: el formato debe ser csv o json.")
        return

    try:
       viajes = fuente.cargar(ruta)
       print(f"Se cargaron {len(viajes)} viajes correctamente.")

       validar_esquema(viajes)
       print("La estructura de los datos es correcta.")
       viajes_validos, viajes_rechazados = validar_recorridos(viajes)

       print(f"Viajes válidos: {len(viajes_validos)}")
       print(f"Viajes rechazados: {len(viajes_rechazados)}")

       

       carpeta_salida = carpeta_proyecto / "outputs"
       carpeta_salida.mkdir(exist_ok=True)

       ruta_rechazos = carpeta_salida / "viajes_rechazados.csv"
       guardar_rechazos(viajes_rechazados, ruta_rechazos)

       print("Archivo de rechazos guardado en outputs/viajes_rechazados.csv")
       if not viajes_validos:
               raise ValueError(
                       "No hay viajes válidos para analizar. "
                       "Todos los registros fueron rechazados."
               )
       
       print("\n=== SELECCIÓN DEL PERÍODO ===")

       fecha_desde = input("Ingresá la fecha y hora inicial (AAAA-MM-DD HH:MM:SS): ")
       fecha_hasta = input("Ingresá la fecha y hora final (AAAA-MM-DD HH:MM:SS): ")

       viajes_seleccionados = seleccionar_periodo(
            viajes_validos, fecha_desde, fecha_hasta
        )

       print(f"Viajes seleccionados: {len(viajes_seleccionados)}")
       movimientos = registrar_movimientos(viajes_seleccionados)

       total_salidas = sum(estacion.salidas for estacion in movimientos.values())
       total_llegadas = sum(estacion.llegadas for estacion in movimientos.values())

       print(f"Estaciones registradas: {len(movimientos)}")
       print(f"Total de salidas: {total_salidas}")
       print(f"Total de llegadas: {total_llegadas}")

       reporte = generar_balance(movimientos)

       total_balance = sum(estacion["balance_neto"] for estacion in reporte)

       print(f"Balance total de las estaciones: {total_balance}")
       if total_balance != 0:
            raise ValueError(
                "El balance total es incorrecto: las llegadas y salidas no coinciden."
            )
       ruta_reporte = carpeta_salida / "reporte_estaciones.csv"

       exportar_reporte(reporte, ruta_reporte)

       print("Reporte guardado en outputs/reporte_estaciones.csv")

    except json.JSONDecodeError:
        print("Error: el archivo JSON tiene un formato incorrecto.")

    except (OSError, ValueError) as error:
        print(f"Error durante el procesamiento: {error}")

if __name__ == "__main__":
    main()
