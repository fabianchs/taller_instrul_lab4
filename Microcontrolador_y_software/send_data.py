import random



import sqlite3
import random
import string
from datetime import date


def send_data_db(autor, vector_list):

    try:
        mi_conexion = sqlite3.connect("database/DAQ")
        cursor = mi_conexion.cursor()

        fecha = date.today()
        canal = 1
        tension = 1
        vector_list_2 = [str(x) for x in vector_list]
        vector = '$'.join(vector_list_2)

        # Insertar los valores en la tabla "medicion"
        cursor.execute("INSERT INTO medicion (autor, fecha, canal, tension, vector) VALUES (?, ?, ?, ?, ?)", (autor, fecha, canal, tension, vector))

        # Confirmar la inserción y cerrar la conexión
        mi_conexion.commit()
        mi_conexion.close()

    except Exception as ex:
        print(ex)


