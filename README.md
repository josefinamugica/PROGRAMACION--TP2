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