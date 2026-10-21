# 2. Documentación de los datos y su procedencia

## Fuente y procedencia de los datos

Para el desarrollo del proyecto se utilizaron datos públicos de los viajes realizados mediante el sistema de bicicletas públicas Ecobici de la Ciudad de Buenos Aires durante el año 2024.

Los datos fueron obtenidos del portal oficial **Buenos Aires Data**, perteneciente al Gobierno de la Ciudad Autónoma de Buenos Aires, específicamente del recurso **"Recorridos Realizados 2024"**, incluido en el conjunto de datos *Bicicletas Públicas*.

- **Fuente:** Buenos Aires Data — Bicicletas Públicas.
- **Organismo responsable:** Secretaría de Transporte y Obras Públicas, Jefatura de Gabinete de Ministros, Gobierno de la Ciudad de Buenos Aires.
- **URL:** https://data.buenosaires.gob.ar/dataset/bicicletas-publicas?
- **Recurso utilizado:** Recorridos Realizados 2024.
- **Licencia:** Creative Commons Atribución 2.5 Argentina (CC BY 2.5 AR), que permite reutilizar los datos reconociendo su procedencia.
- **Fecha de consulta:** 18 de octubre de 2026.

El recurso se descargó como un archivo comprimido ZIP que contiene los registros de viajes en formato CSV. Esta fuente resulta adecuada para el proyecto porque proporciona información sobre las fechas y horas de los recorridos y las estaciones de origen y destino, necesaria para analizar los movimientos de bicicletas.

## Explicacion unidad de análisis y descripcion de variables utilizadas

La **unidad de análisis es cada viaje registrado en el sistema Ecobici**. Por lo tanto, cada fila del archivo representa un recorrido individual, con información sobre su inicio, finalización y estaciones involucradas.

El archivo original contiene 17 variables, de las cuales se seleccionaron las siguientes 7 por su relación directa con el funcionamiento de la aplicación:

| Variable | Descripción y utilidad |
|---|---|
| `id_recorrido` | Identificador de cada viaje. Permite reconocer los recorridos y detectar posibles registros duplicados. |
| `fecha_origen_recorrido` | Fecha y hora de inicio del viaje. Se utiliza para seleccionar los recorridos dentro del período solicitado. |
| `fecha_destino_recorrido` | Fecha y hora de finalización. Permite comprobar la coherencia temporal del recorrido. |
| `id_estacion_origen` | Identificador de la estación donde comienza el viaje. Permite contabilizar las salidas. |
| `id_estacion_destino` | Identificador de la estación donde finaliza el viaje. Permite contabilizar las llegadas. |
| `nombre_estacion_origen` | Nombre de la estación de salida, utilizado para facilitar la lectura de los reportes. |
| `nombre_estacion_destino` | Nombre de la estación de llegada, utilizado para facilitar la lectura de los reportes. |

Las fechas y horas de los registros observados presentan el formato `AAAA-MM-DD HH:MM:SS`, mientras que las estaciones se identifican mediante códigos y nombres.

No se conservaron variables relacionadas con los usuarios, como `id_usuario` o `genero`, porque no son necesarias para resolver el problema planteado.

## Selección y preparación de la muestra

Debido al tamaño del archivo original, se decidió trabajar con una **muestra de 200 registros reales de viajes**, cantidad que supera el mínimo de 50 observaciones establecido en la consigna.

Para obtenerla, se utilizó el script `extraer_muestra_con_errores.py`, que lee el archivo CSV original y selecciona 180 registros que cumplen las condiciones de validación y 20 registros que presentan inconsistencias. En ambos casos, se conservan los valores originales y únicamente las siete variables necesarias para el funcionamiento de la aplicación.

La selección fue **intencional y orientada a comprobar el tratamiento de errores**, por lo que no constituye una muestra aleatoria ni representa la proporción real de registros incorrectos del sistema Ecobici.

Los 200 registros seleccionados se guardaron en `data/viajes_ecobici.csv`. Posteriormente, mediante el script `convertir_json.py`, se generó el archivo `data/viajes_ecobici.json`, que contiene los mismos viajes y campos en formato JSON.

De esta manera, se dispone de dos archivos equivalentes que permiten comprobar la lectura, validación y procesamiento de datos en ambos formatos.

**Los registros no fueron corregidos ni eliminados durante la preparación de la muestra.** La identificación y separación de viajes válidos y rechazados se realiza durante la ejecución de la aplicación mediante la función `validar_recorridos()`. En la prueba realizada, se obtuvieron 180 viajes válidos y 20 rechazados.

## Conservación y reproducibilidad de los datos

Para facilitar la ejecución y reproducción del proyecto, se conservaron los archivos CSV y JSON con la muestra de **200 viajes** dentro de la carpeta `data/` del repositorio.

También se mantienen los scripts utilizados para preparar los datos:

- **`extraer_muestra_con_errores.py`:** permite obtener 200 registros reales del archivo original, seleccionando 180 viajes válidos y 20 con inconsistencias, y conservando las variables necesarias.
- **`convertir_json.py`:** genera una versión JSON equivalente a partir de la muestra CSV.

Además, como se mencionó anteriormente, debido al tamaño del conjunto de datos original, de aproximadamente 783 MB, se optó por conservar una muestra reducida de 200 viajes. Para reproducir la obtención de los datos, se debe descargar el recurso *Recorridos Realizados 2024* desde Buenos Aires Data, descomprimir el archivo y ejecutar el script de extracción, indicando la ubicación del CSV original. Luego, se ejecuta el script de conversión para generar la versión JSON.

Los comandos para ejecutar ambos scripts desde la carpeta principal del proyecto son:

```bash
py extraer_muestra_con_errores.py "ruta_del_archivo_original.csv"
py convertir_json.py
```

Este procedimiento permite volver a generar la muestra a partir del mismo archivo original, sin necesidad de almacenar el conjunto completo en el repositorio. Los archivos CSV y JSON resultantes pueden utilizarse directamente como entradas de la aplicación.

## Limitaciones y restricciones de los datos

Si bien se utilizan registros reales de Ecobici, es importante considerar algunas limitaciones:

- **Tamaño y representatividad:** la muestra contiene 200 registros del archivo original, seleccionados intencionalmente para incluir 180 viajes válidos y 20 con inconsistencias reales. Por lo tanto, no constituye una muestra aleatoria ni garantiza representar todos los períodos, estaciones o movimientos de Ecobici durante 2024. En consecuencia, los resultados obtenidos describen exclusivamente los viajes incluidos en la muestra y no pueden generalizarse al funcionamiento completo del sistema.
- **Calidad de los registros:** la muestra incluye registros con inconsistencias, principalmente relacionadas con las fechas de los recorridos. Estos errores se identifican mediante las validaciones de la aplicación, que separa los viajes válidos de los rechazados y registra los motivos correspondientes.
- **Disponibilidad de información:** los datos permiten analizar movimientos registrados entre estaciones, pero no conocer la cantidad real de bicicletas disponibles, ya que no incluyen el inventario inicial ni las reposiciones.
- **Alcance temporal:** los registros corresponden a viajes de 2024 y no representan el estado actual del sistema Ecobici.

Por último, la muestra conserva únicamente las variables necesarias para el análisis. No se incluyen identificadores de usuarios ni otros datos personales, y el archivo original completo no se incorpora al repositorio debido a su tamaño.

Estas decisiones permiten trabajar con un conjunto de datos pequeño y adecuado para desarrollar, probar y documentar la aplicación, reconociendo las limitaciones de los resultados que se obtengan.
