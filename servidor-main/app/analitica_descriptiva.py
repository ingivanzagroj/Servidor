import datetime
import pandas as pd
import numpy as np
import csv

def update(file_name):
    datos_pandas = leer_datos(file_name)
    funcion_maximo(datos_pandas, file_name)
    funcion_minimo(datos_pandas, file_name)
    funcion_mediana(datos_pandas, file_name) 
    funcion_promedio(datos_pandas, file_name)
    funcion_desviacion(datos_pandas, file_name)   
    """
    Inserte aqui las otras funciones.
    funcion_Minimo()
    funcion_Mediana()
    funcion_Promedio()
    funcion_Desviacion()
    funcion_Varianza()
    """
    datos_graficar = leer_datos(file_name)
    return datos_graficar


def funcion_maximo(datos_pandas, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos_pandas[datos_pandas["sensor"] == "Temperatura"]["value"]
    dat_max=max(valores_temperatura)
    dato_guardar = [1, date_string, "Maximo", dat_max]
    guardar(dato_guardar, file_name)


def funcion_minimo(datos_pandas, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos_pandas[datos_pandas["sensor"] == "Temperatura"]["value"]
    dat_min=min(valores_temperatura)
    dato_guardar = [1, date_string, "Minimo", dat_min]
    guardar(dato_guardar, file_name)


def funcion_mediana(datos_pandas, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos_pandas[datos_pandas["sensor"] == "Temperatura"]["value"]
    dat_mediana=np.median(valores_temperatura)
    dato_guardar = [1, date_string, "Mediana", dat_mediana]
    guardar(dato_guardar, file_name)


def funcion_promedio(datos_pandas, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos_pandas[datos_pandas["sensor"] == "Temperatura"]["value"]
    sumatoria = sum(valores_temperatura)
    longitud = float(len(valores_temperatura))
    resultado = sumatoria / longitud
    dato_guardar = [1, date_string, "Promedio", resultado]
    guardar(dato_guardar, file_name)


def funcion_desviacion(datos_pandas, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos_pandas[datos_pandas["sensor"] == "Temperatura"]["value"]
    dat_desv=np.std(valores_temperatura)
    dato_guardar = [1, date_string, "Desviacion", dat_desv]
    guardar(dato_guardar, file_name)


def funcion_varianza(datos_pandas, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos_pandas[datos_pandas["sensor"] == "Temperatura"]["value"]
    dat_var=pvariance(valores_temperatura)
    dato_guardar = [1, date_string, "Varianza", dat_var]
    guardar(dato_guardar, file_name)


def leer_datos(file_name):
    datos_pandas = pd.read_csv(file_name, index_col=0, parse_dates=True)
    return datos_pandas


def guardar(data, file_name):    
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(data)
