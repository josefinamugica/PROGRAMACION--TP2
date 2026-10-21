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