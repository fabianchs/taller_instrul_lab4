import tkinter
from tkinter import *
import customtkinter  
from PIL import Image
import time
import matplotlib.pyplot  as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

import numpy as np
import serial
import threading
import time
import os
from send_data import send_data_db

#Configuracion del puerto
ard = serial.Serial('COM3',9600)
datos =     []  #Arreglo de datos
datos2 =    []
tiempos=    []  #Arreglo de tiempos
tiempos2=   []

factor = 0.1106729138;
# Función de actualización de la gráfica


lines = [0,0]

vector=[0,0,0]

window_size = 50  # Tamaño de la ventana temporal
def enviar_datos():  
        autor=entry.get()
        try:
            if muestra==1024:
                vector_1 = vector[-1024:]
            else:
                vector_1= vector
            


        except:
            print("la lista no fue accedida correctamente")

        vector_1 = vector
        if autor!="":
            pass
        else:
            autor="no especificado"
        send_data_db(autor, vector_1)

seleccion_1 = "APAGADO"
seleccion_2 = "APAGADO"


tiempo_count = -1 #Variable que ira contanto el tiempo , ira en la funcion de actualizar grafica
read_count =0     #En esta variable se va a guardar las veces que se leyo un dato para saber en que momento enviar el vector a la base de datos

def actualizar_grafica():
    global lines
    global datos
    global datos2
    global tiempos
    global tiempos2
    global seleccion_1
    global tiempo_count
    global read_count
    while True:
        try:   
            linea = ard.readline().decode('utf-8').strip()
            tiempo_count = tiempo_count + 1 #Le sumo al tiempo
            
            
            if seleccion_1 == "APAGADO" and seleccion_2 == "APAGADO" and linea:  #Dentro de la computadora es donde debo tratar los datos para que sea mas rapido
                read_count = read_count + 1
                dato = linea                       #Tomo el dato analogico leido
                dato = float(dato)                 #Lo paso a numero
                dato = dato*factor                 #Lo multiplico por un factor para que ya me de la temperatura correcta
                
                tiempo_actual = tiempo_count       #Igual a la variable de tiempo que ira contando
                
                print("Dato recibido:",dato)       #Verificico que funcione
                #print("Tiempo:",tiempo_actual)

                #datos.append(dato)                 #Agrego el dato a la lista
                #tiempos.append(tiempo_actual)      #Agrego el tiempo a la lista

                #Grafica

                lines[0].set_data(tiempos, datos)
                lines[1].set_data(tiempos2, datos2)
                
                for ax in [ax1, ax2]:
                    ax.relim()
                    ax.autoscale_view()
                fig.canvas.flush_events()

                
                fig.canvas.flush_events()


                #Aqui tengo que cambiar el 2048 por 5000
                
                if len(vector) < 5000: #Si es menor a 5000 entonces solo se agregan los datos
                    vector.append(dato)
                    
                elif len(vector) == 5000: #Si se llena se envia a la base de datos y luego se limpia
                    print("Muestras enviadas")
                    enviar_datos()
                    vector.clear()
                


                    
            if seleccion_1 == "ENCENDIDO" and seleccion_2 == "APAGADO" and linea:
                read_count = read_count + 1
                dato = linea                       #Tomo el dato analogico leido
                dato = float(dato)                 #Lo paso a numero
                dato = dato*factor
                               #Lo multiplico por un factor para que ya me de la temperatura correcta
                tiempo_actual = tiempo_count       #Igual a la variable de tiempo que ira contando
                
                print("Dato recibido:",dato)       #Verificico que funcione
                #print("Tiempo:",tiempo_actual)

                datos.append(dato)                 #Agrego el dato a la lista
                tiempos.append(tiempo_actual)      #Agrego el tiempo a la lista


                #Grafica
                
                lines[0].set_data(tiempos, datos)
                lines[1].set_data(tiempos2, datos2)
                
                for ax in [ax1, ax2]:
                    ax.relim()
                    ax.autoscale_view()
                fig.canvas.flush_events()

                
                fig.canvas.flush_events()

                #Aqui tengo que cambiar el 2048 por 5000
                
                if len(vector) < 5000: #Si es menor a 5000 entonces solo se agregan los datos
                    vector.append(dato)
                    
             
                elif len(vector)== 5000: #Si se llena se envia a la base de datos y luego se limpia
                    print("Muestras enviadas")
                    enviar_datos()
                    vector.clear()
                
                    

            if seleccion_1 == "APAGADO" and seleccion_2 == "ENCENDIDO" and linea:
                read_count = read_count + 1
                dato = linea                       #Tomo el dato analogico leido
                dato = float(dato)                 #Lo paso a numero
                dato = dato*factor                 #Lo multiplico por un factor para que ya me de la temperatura correcta
                
                tiempo_actual = tiempo_count       #Igual a la variable de tiempo que ira contando
                
                print("Dato recibido:",dato)       #Verificico que funcione
                #print("Tiempo:",tiempo_actual)


                
                datos2.append(dato)
                tiempos2.append(tiempo_actual)


                #Grafica
                
                lines[0].set_data(tiempos, datos)
                lines[1].set_data(tiempos2, datos2)
                
                for ax in [ax1, ax2]:
                    ax.relim()
                    ax.autoscale_view()
                fig.canvas.flush_events()

                
                fig.canvas.flush_events()

                #Aqui tengo que cambiar el 2048 por 5000
                
                if len(vector) < 5000: #Si es menor a 5000 entonces solo se agregan los datos
                    vector.append(dato)
                    
                
                elif len(vector)== 5000: #Si se llena se envia a la base de datos y luego se limpia
                    print("Muestras enviadas")
                    enviar_datos()
                    vector.clear()
                
                
            if seleccion_1 == "ENCENDIDO" and seleccion_2 == "ENCENDIDO" and linea:
                read_count = read_count + 1
                dato = linea                       #Tomo el dato analogico leido
                dato = float(dato)                 #Lo paso a numero
                dato = dato*factor                 #Lo multiplico por un factor para que ya me de la temperatura correcta
                
                tiempo_actual = tiempo_count       #Igual a la variable de tiempo que ira contando
                
                print("Dato recibido:",dato)       #Verificico que funcione
                #print("Tiempo:",tiempo_actual)

                
                datos.append(dato)
                datos2.append(dato)
                tiempos.append(tiempo_actual)
                tiempos2.append(tiempo_actual)


                #Grafica
                
                lines[0].set_data(tiempos, datos)
                lines[1].set_data(tiempos2, datos2)
                
                for ax in [ax1, ax2]:
                    ax.relim()
                    ax.autoscale_view()
                fig.canvas.flush_events()

                #Aqui tengo que cambiar el 2048 por 5000
                
                if len(vector) < 5000: #Si es menor a 5000 entonces solo se agregan los datos
                    vector.append(dato)
                    

                elif len(vector)== 5000: #Si se llena se envia a la base de datos y luego se limpia
                    print("Muestras enviadas")
                    enviar_datos()
                    vector.clear()
                    
                    
        except KeyboardInterrupt:
            break
        except ValueError:
            pass
    return



if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")

    customtkinter.set_default_color_theme("green")

    root=customtkinter.CTk()

    root.geometry("850x600")


    text_descripcion=customtkinter.CTkLabel(master=root, text="OSCILOSCOPIO DOS CANALES")
    text_descripcion.place(x=10, y=17)


    #-----------------MATPLOTLIB INICIO

    # Configuración de la figura
    plt.ion()  # Habilita el modo interactivo de Matplotlib
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    fig.suptitle('Osciloscopio de Dos Canales')
    ax1.set_ylabel('Amplitud Canal 1')
    ax2.set_ylabel('Amplitud Canal 2')
    ax2.set_xlabel('Tiempo (s)')
    lines[0] = ax1.plot([], lw=2)[0]
    lines[1] = ax2.plot([], lw=2)[0]

    for ax in [ax1, ax2]:
        #ax.set_xlim(0, 50)  # Rango temporal
        #ax.set_ylim(-1, 10)  # Rango de amplitud
        ax.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().place(x=10, y=50)
    plt.close('all')

    #-------- BOTON DE INICIAR

    button=customtkinter.CTkButton(master=root, text="Iniciar", fg_color="green",command = actualizar_grafica)

    button.place(x=690, y=450)


    # ------------- BOTON DE INICIAR FINAL



    #------ MUESTRAS INICIO
    radio_var = tkinter.IntVar()
    muestra=1024
    def radiobutton_event():
        muestra=radio_var.get()
        print (muestra)

    button_2=customtkinter.CTkRadioButton(master=root, text="1024", command=radiobutton_event, variable= radio_var, value=1024 )
    button_2.place( x=690, y=20)

    button_2=customtkinter.CTkRadioButton(master=root, text="2048", command=radiobutton_event ,variable= radio_var, value=2048  )
    button_2.place( x=770, y=20)

    text_muestras=customtkinter.CTkLabel(master=root, text="MUESTRAS :")
    text_muestras.place(x=580, y=17)

    text_muestras_2=customtkinter.CTkLabel(master=root, text="1024 por default", text_color="orange")
    text_muestras_2.place(x=580, y=50)

    #------- MUESTRAS FIN

            #-------- BOTON GUARDAR INICIO
    #Ideas, meter esto dentro de la funcion 
    
        

    button=customtkinter.CTkButton(master=root, text="GUARDAR", fg_color="violet",command = enviar_datos)

    button.place(x=690, y=50)


    # ------------- BOTON GUARDAR FINAL

    #------------USUARIO INICIO

    entry = customtkinter.CTkEntry(master=root, placeholder_text="USUARIO")
    entry.place(x=690,y=90)

    text_muestras=customtkinter.CTkLabel(master=root, text="Inserte usuario :")
    text_muestras.place(x=580, y=89)
    #--------------USUARIO FIN


    #--------------FUNCIONES CANALES INICIO

    combobox_ch1_onoff = customtkinter.StringVar(value="ENCENDIDO")

    combobox_ch1_magnitude=customtkinter.StringVar(value="Tension[V]")



    def on_off_1(seleccion):
        global seleccion_1
        seleccion_1=seleccion
        if seleccion=="ENCENDIDO":
            ax1.set_ylabel("Tension[V]", color='g')
            fig.canvas.flush_events()
            
        else:
            ax1.set_ylabel("", color='g')
            datos.clear()
            tiempos.clear()
        fig.canvas.flush_events()

    def enviar_comando_arduino(comando):
        try:
            time.sleep(2)  # Espera a que se establezca la conexión
            ard.write(str(comando).encode())
            print(f"Enviado comando {comando} a Arduino")
        except Exception as e:
            print(f"Error al comunicarse con Arduino: {e}")


    def magnitude_1(magnitud):
        magnitudes = ["10V","8V","5V","1V","100mV", "10mV"]

        if magnitud in magnitudes:
            print(magnitud)
            comando = magnitudes.index(magnitud) + 1
            print(comando)
            enviar_comando_arduino(comando)
        else:
            print("Magnitud no válida")

    #--------------FUNCIONES CANALES FINAL

    #------------CANAL 1 INICIO

    behind_box_1=customtkinter.CTkFrame(master=root, fg_color="transparent",border_width=3, border_color="white", width=260, height=110)
    behind_box_1.place(x=570,y=140)

    text_canal_1=customtkinter.CTkLabel(master=root, text="CANAL 1", text_color="white")
    text_canal_1.place(x=580, y=160)

    switch_var = customtkinter.StringVar(value="on")


    conversion_1=customtkinter.CTkComboBox(master=root, values=["ENCENDIDO", "APAGADO"], command=on_off_1, variable=combobox_ch1_onoff)
    conversion_1.place(x=680, y=160)


    text_conversion_1=customtkinter.CTkLabel(master=root, text="Escala:", text_color="white")
    text_conversion_1.place(x=580, y=200)


    conversion_1=customtkinter.CTkComboBox(master=root, values=["10V","8V","5V","1V","100mV", "10mV", "Fahrenheit","Kelvin"],command=magnitude_1, variable=combobox_ch1_magnitude)
    conversion_1.place(x=680, y=200)

    #text_escala_1=customtkinter.CTkLabel(master=root, text="Escala :", text_color="white")
    #text_escala_1.place(x=580, y=240)

    #escala_1=customtkinter.CTkComboBox(master=root, values=["uV","mV","V","kV","MV ", "Celsius", "Fahrenheit","Kelvin"])
    #escala_1.place(x=680, y=240)

    #------------CANAL 1 FIN

    #--------------FUNCIONES CANALES FINAL

    #--------------FUNCIONES CANALES INICIO
    combobox_ch2_magnitude=customtkinter.StringVar(value="Tension[V]")
    combobox_ch2_onoff = customtkinter.StringVar(value="ENCENDIDO")

    def on_off_2(seleccion):
        global seleccion_2
        seleccion_2 = seleccion
        if seleccion=="ENCENDIDO":
            ax2.set_ylabel("Tension[V]", color='b')
            fig.canvas.flush_events()
        else:
            ax2.set_ylabel("", color='b')
            datos2.clear()
            tiempos2.clear()
            
        fig.canvas.flush_events()



    def magnitude_2(magnitud):
        print(seleccion_2)
        if seleccion_2=="ENCENDIDO":
            ax2.set_ylabel(magnitud, color='b')
            canvas.draw()
        else:
            ax2.set_ylabel("", color='b')
            canvas.draw()


    #--------------FUNCIONES CANALES FINAL

    #------------CANAL 2 INICIO

    behind_box_2=customtkinter.CTkFrame(master=root, fg_color="transparent",border_width=3, border_color="white", width=260, height=110)
    behind_box_2.place(x=570,y=260)

    text_canal_2=customtkinter.CTkLabel(master=root, text="CANAL 2", text_color="white")
    text_canal_2.place(x=580, y=280)

    switch_var_2 = customtkinter.StringVar(value="on")


    conversion_2=customtkinter.CTkComboBox(master=root, values=["ENCENDIDO", "APAGADO"], command=on_off_2, variable=combobox_ch2_onoff)
    conversion_2.place(x=680, y=280)


    text_conversion_2=customtkinter.CTkLabel(master=root, text="Escala :", text_color="white")
    text_conversion_2.place(x=580, y=320)

    conversion_2=customtkinter.CTkComboBox(master=root, values=["Tension[uV]","Tension[mV]","Tension[V]","Tension[kV]","Tension[MV]", "Celsius", "Fahrenheit","Kelvin"],command=magnitude_2, variable=combobox_ch2_magnitude)
    conversion_2.place(x=680, y=320)

    #text_escala_1=customtkinter.CTkLabel(master=root, text="Escala :", text_color="white")
    #text_escala_1.place(x=580, y=240)

    #escala_1=customtkinter.CTkComboBox(master=root, values=["uV","mV","V","kV","MV ", "Celsius", "Fahrenheit","Kelvin"])
    #escala_1.place(x=680, y=240)

    #------------CANAL 1 FIN


    # Bucle principal


    root.mainloop()



    
    


    
   

