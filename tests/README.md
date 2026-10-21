##  Verificación del comportamiento y pruebas automáticas

El proyecto incluye pruebas automáticas desarrolladas con `unittest`, que permiten verificar el comportamiento esperado de la aplicación y comprobar que las funciones implementadas producen resultados correctos.

###  Pruebas correspondientes a los requisitos obligatorios

1. **Caso normal (`test_viaje_normal`):** comprueba que un viaje válido desde la estación A hacia la estación B genere una salida en el origen, una llegada en el destino y los balances correspondientes.

2. **Entrada inválida (`test_fecha_invalida`):** verifica que un viaje con una fecha inexistente, como el 30 de febrero, sea rechazado y se registre el motivo correspondiente.

3. **Propiedad relevante del resultado (`test_conservacion_movimientos`):** comprueba la conservación de cantidades: cada viaje válido genera una salida y una llegada, por lo que el total de salidas debe coincidir con el total de llegadas y la suma de los balances debe ser cero.

###  Pruebas adicionales

4. **Viaje duplicado (`test_viaje_duplicado`):** comprueba que, ante dos viajes con el mismo identificador, se conserve el primero válido y se rechace el repetido.

5. **Estación faltante (`test_estacion_faltante`):** verifica que un viaje con información incompleta de una estación sea rechazado y se registre el motivo correspondiente.

6. **Falla de lectura (`test_archivo_inexistente`):** comprueba que, al intentar leer un archivo CSV inexistente, se produzca un error en lugar de ocultar la falla.

7. **Finalización anterior al inicio (`test_finalizacion_anterior_al_inicio`):** comprueba que un viaje cuya fecha y hora de finalización sean anteriores a las de inicio sea rechazado y no genere movimientos en ninguna estación.

Estas pruebas también permiten verificar aspectos adicionales de calidad exigidos por la consigna: la validación de resultados importantes, el tratamiento explícito de valores faltantes, duplicados y fechas inválidas, y la detección de fallas de lectura. De esta manera, se comprueba que la aplicación no solo procesa viajes válidos, sino que también reconoce determinadas inconsistencias y evita que afecten los resultados.

###   Ejecución de las pruebas

Para ejecutar todas las pruebas, abrir una terminal en la carpeta principal del proyecto e ingresar:

```powershell
py -m unittest discover -s tests -p "test_*.py" -v
```

El comando ejecuta automáticamente las seis pruebas. Si todas se cumplen correctamente, la terminal muestra `OK`. En caso contrario, informa cuál falló.