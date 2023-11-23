# Documentacion
## Esquemático final
![circuito final](https://github.com/fabianchs/taller_instrul_lab4/assets/26722437/471e3ac4-8fee-4116-a4fd-ce971efce288)

## Circuito del sistema

![1](https://github.com/fabianchs/taller_instrul_lab4/assets/26722437/1d51dee5-63ba-40bf-97ad-572059a0d779)

![2](https://github.com/fabianchs/taller_instrul_lab4/assets/26722437/4e6c7639-5048-414a-a02b-6a5f3b0f284e)

## Medición de desempeño
Para esta etapa se usó un lcd con el cual se podía visualizar en tiempo real los cambios de temperatura, sin embargo, para aumentar la velocidad de transferencia de información se opto por enviar datos “Crudos” al pc y que este se encargara de procesarlos para traducirlos a valores de temperatura legibles con una tasa de 5000 datos por segundo, pero para facilitar los experimentos se uso una tasa de 2 datos por segundo, ya que, cada experimento duraba aproximadamente una hora y treinta minutos.

## Análisis de datos
Se realizó un código en python para analizar los datos obtenidos, los pasos que sigue el código se explican a continuación.

### 1.Lectura del archivo CSV:

Se utiliza la función leer_csv para leer los datos del archivo CSV especificado.
Los datos se almacenan en el arreglo arreglo_resultante.

### 2.Decimación de Muestras:

El arreglo original arreglo_resultante se le aplica la técnica de "decimación", reduciendo la cantidad de muestras por un factor de 10. El resultado se almacena en arreglo_decimado.

### 3.Cálculo de la Constante k:

Se realiza un bucle sobre las temperaturas decimadas, y se calcula la constante
k utilizando la fórmula k=(1/t_inicial) * (math.log((temperatura - 26) / C)).
Se realiza un promedio de las constantes k calculadas y se almacena en k_final.

### 4.Filtrado de Media Móvil:

Se aplica un filtro de media móvil a las temperaturas decimadas antes de calcular k.
Posteriormente, se realiza un segundo filtrado de media móvil con una ventana de 200 elementos y se almacena en arreglo_filtrado.

### 5.Cálculo de Porcentaje de Error:

Se calcula el porcentaje de error entre las temperaturas obtenidas del modelo Newtoniano y las temperaturas filtradas.
Se realiza un bucle sobre los datos y se calcula el porcentaje de error promedio.

### 6.Graficación de Resultados:
Se grafican las temperaturas obtenidas del modelo Newtoniano y las temperaturas filtradas en función del tiempo.
Se incluyen anotaciones en el gráfico para mostrar el valor de k y el porcentaje de error promedio.

Se realizaron 3 experimentos diferentes de los cuales se obtuvieron las siguientes gráficas:

### Experimento 1
![image](https://github.com/fabianchs/taller_instrul_lab4/assets/26722437/8fb36660-d962-404e-8b33-26ed71f19ad8)

### Experimento 2
![image](https://github.com/fabianchs/taller_instrul_lab4/assets/26722437/7cf7f1f6-3db2-49c7-bd4a-ba49ce1bff7e)

### Experimento 3
![image](https://github.com/fabianchs/taller_instrul_lab4/assets/26722437/1cab1872-4e9a-4a46-97c8-fba583e32262)

El experimento 3 es el que dio mejores resultados a nivel de modelado con un error de 2.66% y un valor k de 0.19.

Algunas razones por las cuales los experimentos 1 y 2 no se aproximaron correctamente puede ser ocasionado por:

1.Lecturas incorrectas del circuito de medición
2.Valores muy desviados de las temperaturas reales obtenidas
3.Cambios en las condiciones atmosféricas durante la realización del experimento

## Divulgación
https://www.hackster.io/fabian-chacon/obtencion-de-modelo-de-enfriamiento-a-partir-de-experimento-d6a51e
