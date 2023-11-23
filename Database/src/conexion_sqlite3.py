import sqlite3

try:
    mi_conexion=sqlite3.connect("database\DAQ")
    cursor=mi_conexion.cursor()
    cursor.execute("DROP TABLE medicion")
    cursor.execute("CREATE TABLE medicion (autor VARCHAR(50), fecha DATE, canal INTEGER, tension FLOAT,  vector VARCHAR(10240))")
except Exception as ex:
    print(ex)
