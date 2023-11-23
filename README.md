# Documentacion
#Esquemático final

# Medición de desempeño

## Análisis de datos
Se realizó un código en python para analizar los datos obtenidos, los pasos que sigue el código se explican a continuación.

1.Lectura del archivo CSV:

Se utiliza la función leer_csv para leer los datos del archivo CSV especificado.
Los datos se almacenan en el arreglo arreglo_resultante.

2.Decimación de Muestras:

El arreglo original arreglo_resultante se le aplica la técnica de "decimación", reduciendo la cantidad de muestras por un factor de 10. El resultado se almacena en arreglo_decimado.

3.Cálculo de la Constante k:

Se realiza un bucle sobre las temperaturas decimadas, y se calcula la constante
k utilizando la fórmula k=(1/t_inicial) * (math.log((temperatura - 26) / C)).
Se realiza un promedio de las constantes k calculadas y se almacena en k_final.

4.Filtrado de Media Móvil:

Se aplica un filtro de media móvil a las temperaturas decimadas antes de calcular k.
Posteriormente, se realiza un segundo filtrado de media móvil con una ventana de 200 elementos y se almacena en arreglo_filtrado.

5.Cálculo de Porcentaje de Error:

Se calcula el porcentaje de error entre las temperaturas obtenidas del modelo Newtoniano y las temperaturas filtradas.
Se realiza un bucle sobre los datos y se calcula el porcentaje de error promedio.

6.Graficación de Resultados:
Se grafican las temperaturas obtenidas del modelo Newtoniano y las temperaturas filtradas en función del tiempo.
Se incluyen anotaciones en el gráfico para mostrar el valor de k y el porcentaje de error promedio.

#Divulgación
https://www.hackster.io/fabian-chacon/obtencion-de-modelo-de-enfriamiento-a-partir-de-experimento-d6a51e
