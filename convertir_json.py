
import csv
import json

# Archivo CSV que ya creamos
archivo_csv = "data/viajes_ecobici.csv"

# Archivo JSON que vamos a generar
archivo_json = "data/viajes_ecobici.json"

# Leer los viajes del CSV
with open(archivo_csv, "r", encoding="utf-8", newline="") as archivo:
    lector = csv.DictReader(archivo)
    viajes = list(lector)

# Guardar los mismos viajes en formato JSON
with open(archivo_json, "w", encoding="utf-8") as archivo:
    json.dump(viajes, archivo, indent=4, ensure_ascii=False)

print(f"Archivo JSON creado con {len(viajes)} viajes.")
