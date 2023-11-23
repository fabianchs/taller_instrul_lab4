import csv
import numpy as np
import math
import matplotlib.pyplot as plt
import csv

nombre_archivo="EX3.csv"
def leer_csv(nombre_archivo):
    arreglo_numeros = []

    with open(nombre_archivo, 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        
        # Suponemos que los números están en la columna A (índice 0)
        for fila in lector_csv:
            try:
                numero = float(fila[0])
                arreglo_numeros.append(numero)
            except ValueError:
                # Ignorar las filas que no contienen números válidos
                pass

    return np.array(arreglo_numeros)

nombre_archivo_csv = 'EX3.csv'
arreglo_resultante = leer_csv(nombre_archivo_csv)

C = arreglo_resultante[0] - 26

# Decimar las muestras
factor_decimacion = 10
arreglo_decimado = np.array(arreglo_resultante[::factor_decimacion])

t_inicial = 0.002*10
k_valores = []
tiempos = []
temperaturas = []
for temperatura in arreglo_decimado:
    try:
        if 20 < temperatura < 61:
            k = (1/t_inicial) * (math.log((temperatura - 26) / C))
            tiempos.append(t_inicial)
            t_inicial += 0.0002*10
            k_valores.append(k)
            temperaturas.append(temperatura)
    except:
        pass

try:
    k_valores.remove(0)
except:
    pass
k_final = sum(k_valores) / len(k_valores)

print(k_final)

# Parámetros del filtro de media móvil
ventana = 5  # Tamaño de la ventana de media móvil

# Aplicar filtro de media móvil a las temperaturas antes de calcular k
arreglo_filtrado = np.convolve(temperaturas, np.ones(ventana)/ventana, mode='valid')
arreglo_mega_filtrado=[]
for i in range(0, len(arreglo_filtrado)):
    try:
        elements=arreglo_filtrado[i:i+200]
        average=sum(elements)/len(elements)
        arreglo_mega_filtrado.append(average)
    except:
        pass

arreglo_filtrado=arreglo_mega_filtrado
# Ejemplo de lista de temperaturas y tiempos
print(len(arreglo_filtrado))
minutes = 17
relation = minutes / len(arreglo_filtrado)
times_relation = np.linspace(0, minutes, len(arreglo_filtrado))

# Definir temperatura ambiente
Ta = 26

# Definir función de enfriamiento
def temperatura_enfriamiento(t, T0, Ta, k):
    return Ta + (T0 - Ta) * np.exp(-k * t)



# Calcular las temperaturas en función del tiempo con el modelo filtrado
temperaturas_modelo = temperatura_enfriamiento(times_relation, arreglo_filtrado[0], Ta, -k_final)

porcentajes_error=[]

def calcular_porcentaje_error(y_real, y_pred):
    errores = np.abs(y_real - y_pred) / np.abs(y_real)
    porcentaje_error = np.mean(errores) * 100
    return porcentaje_error

for i in range(0, len(temperaturas_modelo)):
    error=calcular_porcentaje_error(arreglo_filtrado[i],temperaturas_modelo[i])
    porcentajes_error.append(error)

error_final= sum(porcentajes_error) / len(porcentajes_error)
print(error_final)

# Graficar temperatura vs tiempo con la señal filtrada
plt.plot(times_relation, temperaturas_modelo, label='Modelo Newtoniano Filtrado')
plt.plot(times_relation, arreglo_filtrado, label='Datos Filtrados', linestyle='dashed')

plt.text(13, 51, 'k='+str(round(-k_final,2)))
plt.text(13, 53, 'error='+str(round(error_final,2)))
plt.legend()
plt.title('Enfriamiento Newtoniano con Decimación y Filtro de Media Móvil')
plt.xlabel('Tiempo (minutos)')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.show()
