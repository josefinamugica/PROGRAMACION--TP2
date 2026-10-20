# TP2 - Reporte de movimientos de Ecobici

**Materia:** Programación Orientada a Datos  
**Universidad:** Universidad Católica Argentina (UCA)  
**Trabajo:** Trabajo Práctico 2 - Individual  
**Autor:** Josefina Mugica

---
# 1. Definición del problema y alcance

## 1.1. Problema o necesidad

El sistema de bicicletas públicas Ecobici de la Ciudad de Buenos Aires permite realizar viajes entre diferentes estaciones. Cada viaje genera un registro con información como su identificador, la fecha y hora de inicio y finalización, y las estaciones de origen y destino.

Para analizar el funcionamiento de esta red, es necesario conocer **cuántos viajes comienzan y terminan en cada estación durante un período determinado**. Esta información permite identificar los movimientos registrados y conocer la diferencia entre las salidas y las llegadas de bicicletas en cada estación.

Sin embargo, los archivos de viajes pueden contener **registros incompletos, inconsistentes o duplicados**, como viajes sin estación de destino, fechas incorrectas o movimientos registrados más de una vez. Si estos datos se utilizan sin verificarlos, pueden producir resultados equivocados y alterar los balances de las estaciones.

Por este motivo, surge la necesidad de contar con una herramienta que permita procesar los registros de viajes, identificar aquellos que presentan errores y generar información confiable sobre los movimientos de bicicletas.

## 1.2. Usuarios y utilidad

La aplicación está dirigida principalmente a personas encargadas de revisar el funcionamiento del sistema Ecobici, así como a estudiantes e investigadores interesados en analizar sus registros de viajes.

Su principal utilidad será **facilitar el seguimiento de los movimientos de bicicletas entre estaciones**, permitiendo conocer la cantidad de salidas y llegadas durante un período seleccionado.

A partir de esta información, los usuarios podrán identificar estaciones donde se registraron más salidas que llegadas, estaciones donde ocurrió lo contrario y aquellas donde ambas cantidades fueron iguales.

De esta manera, la aplicación permitirá consultar y analizar los movimientos registrados sin necesidad de revisar y calcular manualmente cada viaje.

## 1.3. Solución propuesta y funcionalidades

Se desarrollará una **aplicación en Python que procese registros de viajes de Ecobici y genere reportes de movimientos por estación** durante un período determinado.

La aplicación permitirá realizar las siguientes operaciones:

1. **Cargar los datos:** leer archivos de viajes en formatos CSV y JSON que contengan la información necesaria para el análisis.

2. **Validar los registros:** comprobar que los viajes tengan los datos requeridos, que las fechas y horas sean válidas, que la finalización no sea anterior al inicio y que estén identificadas las estaciones de origen y destino.

3. **Detectar registros duplicados:** identificar viajes repetidos a partir de su identificador, aplicando un criterio definido para evitar que un mismo viaje sea contabilizado más de una vez.

4. **Registrar los viajes rechazados:** separar los registros que no cumplan las condiciones establecidas e indicar el motivo por el cual fueron excluidos del análisis.

5. **Seleccionar un período:** permitir que el usuario indique una fecha y hora inicial y una final para analizar los viajes. La selección se realizará considerando el momento de inicio de cada viaje.

6. **Registrar los movimientos:** contabilizar una salida en la estación de origen y una llegada en la estación de destino por cada viaje válido seleccionado, incluso cuando la finalización del viaje ocurra fuera del período solicitado.

7. **Calcular el balance neto:** obtener, para cada estación, la diferencia entre la cantidad de llegadas y salidas registradas.

8. **Generar y exportar un reporte:** presentar los resultados organizados por estación, mostrando las salidas, las llegadas y el balance neto correspondiente. También se conservará un listado de los registros rechazados con sus respectivos motivos.

Estas operaciones permitirán transformar los registros originales en información organizada y útil para analizar los movimientos de la red Ecobici.

## 1.4. Resultados esperados e interpretación

El principal resultado de la aplicación será un **reporte de movimientos por estación**, elaborado a partir de los viajes válidos que comiencen dentro del período seleccionado.

Para cada estación, el reporte mostrará:

- **Salidas:** cantidad de viajes que comenzaron en esa estación.
- **Llegadas:** cantidad de viajes que finalizaron en esa estación.
- **Balance neto:** diferencia entre la cantidad de llegadas y salidas.

El balance neto se calculará mediante la siguiente fórmula:

**Balance neto = Llegadas − Salidas**

Su interpretación será la siguiente:

- **Balance positivo:** se registraron más llegadas que salidas.
- **Balance negativo:** se registraron más salidas que llegadas.
- **Balance igual a cero:** se registró la misma cantidad de llegadas y salidas.

Además, el programa permitirá conocer qué registros fueron rechazados y por qué motivo, de manera que los resultados puedan interpretarse teniendo en cuenta los datos que efectivamente participaron en el análisis.

Como comprobación general, **la suma de los balances de todas las estaciones deberá ser igual a cero**, ya que cada viaje válido genera una salida en una estación y una llegada en otra.

## 1.5. Alcance de la primera versión y limitaciones

La primera versión de la aplicación se concentrará en **analizar los movimientos de bicicletas entre estaciones a partir de los registros de viajes de Ecobici**.

Para ello, se utilizarán los siguientes datos:

- Identificador del viaje.
- Fecha y hora de inicio.
- Fecha y hora de finalización.
- Estación de origen.
- Estación de destino.

El usuario podrá seleccionar un período de análisis y generar un reporte con las salidas, llegadas y balances netos de las estaciones involucradas.

Se trabajará únicamente con los viajes que superen las validaciones establecidas, evitando que los registros incorrectos o duplicados alteren los resultados.

**La aplicación tendrá las siguientes limitaciones:**

- No permitirá conocer la cantidad real de bicicletas disponibles en cada estación, ya que no considerará el inventario inicial, las reposiciones ni otros movimientos que no estén registrados como viajes.
- No realizará un seguimiento de los movimientos en tiempo real, sino que analizará archivos de datos previamente obtenidos.
- No incluirá predicciones sobre la demanda futura de bicicletas.
- No contará con una interfaz web; su funcionamiento se realizará mediante la ejecución del programa en Python.

De esta manera, se busca desarrollar una aplicación de alcance reducido, funcional y verificable, que permita resolver el problema planteado y pueda ampliarse en futuras versiones.
-------------------------------------------------------------------------------------------------------------------------

## 2. Datos utilizados y procedencia

La información detallada sobre la procedencia de los datos, la licencia, las variables seleccionadas, la preparación de la muestra y sus limitaciones se encuentra documentada en [data/README.md](data/README.md).

A modo de síntesis, para este proyecto se utilizaron registros reales de viajes de **Ecobici de la Ciudad de Buenos Aires**, obtenidos del recurso *«Recorridos Realizados 2024»*, disponible en el portal oficial [Buenos Aires Data](https://data.buenosaires.gob.ar/dataset/bicicletas-publicas), bajo la licencia **Creative Commons Atribución 2.5 Argentina (CC BY 2.5 AR)**.

La **unidad de análisis es cada viaje registrado**. Se trabaja con una muestra de 100 viajes, conservando siete variables relacionadas con sus identificadores, fechas y estaciones de origen y destino.

Los datos se encuentran disponibles en `data/viajes_ecobici.csv` y `data/viajes_ecobici.json`, que contienen los mismos registros en ambos formatos.
--------------------------------------------------------------------------------------------------------------------------
## 3. Instalación, ejecución y modo de uso

La aplicación está desarrollada en Python y se ejecuta desde la terminal. Para utilizarla, es necesario tener Python instalado y disponer de los archivos del proyecto.

### 3.1. Requisitos e instalación

El repositorio contiene los archivos necesarios para ejecutar la aplicación, incluidos los datos de ejemplo en formatos CSV y JSON.

El procesamiento utiliza módulos de la biblioteca estándar de Python, por lo que no requiere instalar bibliotecas externas para su funcionamiento principal.

### 3.2. Ejecución de la aplicación

Desde la carpeta principal del proyecto, ejecutar el siguiente comando:

```powershell
py src/main.py
```

Al iniciar, el programa solicitará:

1. **Formato de los datos:** seleccionar `csv` o `json`. La aplicación cargará el archivo correspondiente desde la carpeta `data/`.
2. **Período de análisis:** ingresar una fecha y hora inicial y una final, utilizando el formato `AAAA-MM-DD HH:MM:SS`.

El programa validará los registros y seleccionará los viajes válidos cuya fecha y hora de inicio se encuentren dentro del período indicado.

### 3.3. Resultados generados

Durante la ejecución, la terminal mostrará la cantidad de viajes cargados, válidos, rechazados y seleccionados, así como los totales de salidas, llegadas y el balance general.

Además, se generarán dos archivos en la carpeta `outputs/`:

- **`reporte_estaciones.csv`:** contiene las estaciones involucradas, sus salidas, llegadas y balances netos.
- **`viajes_rechazados.csv`:** registra los viajes excluidos del análisis y el motivo de su rechazo.

La carpeta `outputs/` se crea automáticamente y sus archivos no se incorporan al repositorio, ya que pueden volver a generarse al ejecutar la aplicación.
-------------------------------------------------------------------------------------------------------------------------

## 4. Verificación del comportamiento y pruebas automáticas

El proyecto incluye pruebas automáticas desarrolladas con `unittest`, que permiten verificar el comportamiento esperado de la aplicación y comprobar que las funciones implementadas producen resultados correctos.

### 4.1 Pruebas correspondientes a los requisitos obligatorios

1. **Caso normal (`test_viaje_normal`):** comprueba que un viaje válido desde la estación A hacia la estación B genere una salida en el origen, una llegada en el destino y los balances correspondientes.

2. **Entrada inválida (`test_fecha_invalida`):** verifica que un viaje con una fecha inexistente, como el 30 de febrero, sea rechazado y se registre el motivo correspondiente.

3. **Propiedad relevante del resultado (`test_conservacion_movimientos`):** comprueba la conservación de cantidades: cada viaje válido genera una salida y una llegada, por lo que el total de salidas debe coincidir con el total de llegadas y la suma de los balances debe ser cero.

### 4.2 Pruebas adicionales

4. **Viaje duplicado (`test_viaje_duplicado`):** comprueba que, ante dos viajes con el mismo identificador, se conserve el primero válido y se rechace el repetido.

5. **Estación faltante (`test_estacion_faltante`):** verifica que un viaje con información incompleta de una estación sea rechazado y se registre el motivo correspondiente.

6. **Falla de lectura (`test_archivo_inexistente`):** comprueba que, al intentar leer un archivo CSV inexistente, se produzca un error en lugar de ocultar la falla.

Estas pruebas también permiten verificar aspectos adicionales de calidad exigidos por la consigna: la validación de resultados importantes, el tratamiento explícito de valores faltantes, duplicados y fechas inválidas, y la detección de fallas de lectura. De esta manera, se comprueba que la aplicación no solo procesa viajes válidos, sino que también reconoce determinadas inconsistencias y evita que afecten los resultados.

### 4.3  Ejecución de las pruebas

Para ejecutar todas las pruebas, abrir una terminal en la carpeta principal del proyecto e ingresar:

```powershell
py -m unittest discover -s tests -p "test_*.py" -v
```

El comando ejecuta automáticamente las seis pruebas. Si todas se cumplen correctamente, la terminal muestra `OK`. En caso contrario, informa cuál falló.
-------------------------------------------------------------------------------------------------------------------------

## 5. Organización y estructura del proyecto

El proyecto se organiza en carpetas y archivos que permiten separar las distintas responsabilidades de la aplicación, facilitando su comprensión, mantenimiento y verificación.

### 5.1. Estructura del proyecto

```text
PROGRAMACION-TP2/
│
├── data/
│   ├── README.md
│   ├── viajes_ecobici.csv
│   └── viajes_ecobici.json
│
├── src/
│   ├── dominio.py
│   ├── fuentes.py
│   ├── main.py
│   └── pipeline.py
│
├── tests/
│   └── test_ecobici.py
│
├── convertir_json.py
├── extraer_muestra.py
├── requirements.txt
├── .gitignore
└── README.md
```

### 5.2. Organización del código

El funcionamiento de la aplicación se distribuye principalmente entre cuatro módulos:

- **`main.py`:** coordina la ejecución y conecta las diferentes etapas del procesamiento.
- **`fuentes.py`:** contiene las clases encargadas de leer archivos CSV y JSON mediante una interfaz común.
- **`pipeline.py`:** reúne las funciones de validación, selección, procesamiento y generación de resultados.
- **`dominio.py`:** define la clase `BalanceEstacion`, responsable de registrar los movimientos de cada estación y calcular su balance.

Por su parte, `tests/` contiene las pruebas automáticas, mientras que `data/` reúne los archivos de entrada y su documentación. Los scripts `extraer_muestra.py` y `convertir_json.py` permiten reproducir la preparación de los datos.

Esta estructura permite mantener separados los componentes del proyecto y facilita la revisión de su funcionamiento.
--------------------------------------------------------------------------------------------------------------------
## 6. Ejemplo de ejecución y resultados

Para ejemplificar el funcionamiento de la aplicación, se procesó la muestra de 100 viajes de Ecobici utilizando el archivo `data/viajes_ecobici.csv`.

Se seleccionó el período comprendido entre el **23 de enero de 2024 a las 00:00:00 y las 23:59:59**.

Los resultados obtenidos fueron los siguientes:

| Indicador | Resultado |
|---|---:|
| Viajes cargados | 100 |
| Viajes válidos | 100 |
| Viajes rechazados | 0 |
| Viajes seleccionados | 86 |
| Estaciones registradas | 110 |
| Total de salidas | 86 |
| Total de llegadas | 86 |
| Balance global | 0 |

A partir de los viajes seleccionados, la aplicación generó el archivo `outputs/reporte_estaciones.csv`, que contiene las salidas, llegadas y balances netos correspondientes a cada estación.

También se generó `outputs/viajes_rechazados.csv`, que en esta ejecución no contiene registros rechazados, ya que todos los viajes de la muestra superaron las validaciones establecidas.
----------------------------------------------------------------------------------------------------------------

## 7. Decisiones de validación y limpieza de los datos

Antes de realizar el análisis, la aplicación verifica que los registros cumplan las condiciones necesarias para contabilizar correctamente los movimientos entre estaciones.

Se adoptó como criterio **conservar los viajes válidos y separar aquellos que presenten inconsistencias**, sin modificar los valores originales ni completar datos faltantes de manera artificial.

Las principales reglas de validación son:

- **Identificadores faltantes:** se rechazan los viajes cuyo identificador esté vacío o sea nulo.
- **Viajes duplicados:** se conserva la primera aparición válida de cada identificador y se rechazan las repeticiones, evitando contabilizar un mismo recorrido más de una vez.
- **Estaciones incompletas:** se rechazan los registros que no tengan identificados correctamente el origen o el destino, incluyendo identificadores no numéricos y nombres faltantes.
- **Fechas inválidas:** se comprueba que las fechas respeten el formato `AAAA-MM-DD HH:MM:SS` y correspondan a fechas y horas reales.
- **Inconsistencias temporales:** se rechazan los viajes cuya fecha y hora de finalización sean anteriores a las de inicio.

Los registros rechazados se excluyen de los cálculos y se guardan en `outputs/viajes_rechazados.csv`, junto con el motivo correspondiente. De esta manera, se mantiene un registro de las exclusiones realizadas durante el procesamiento.

Si no queda ningún viaje válido, la aplicación informa el problema y detiene el análisis, conservando previamente el archivo de rechazos.

Estas decisiones buscan evitar que los datos incompletos, duplicados o inconsistentes alteren los conteos y balances de las estaciones.
---------------------------------------------------------------------------------------------------------------