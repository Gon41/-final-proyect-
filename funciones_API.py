import pandas as pd                                    # Importo las librerias necesarias
import numpy as np
from pandas import DataFrame
import requests
from dotenv import load_dotenv
import os
import re
import json
from pandas.io.json import json_normalize




##### FUNCIÓN 1: LLAMADA A LA API #####

def data_api(ll,query,limit,name_database):
    
    load_dotenv()                                           # Importar el acceso al archivo
    
    url = 'https://api.foursquare.com/v2/venues/explore'    # Dirección de la API
   
    params = dict(
    client_id=os.getenv("FQ_CLIENT_ID"),                    # Verificación ID de acceso          
    client_secret=os.getenv("FQ_CLIENT_SECRET"),            # Verificación claves de acceso
    v='20201201',                                           # Fecha de actualización
    ll=ll,
    radius="10000",                                           # Coordenadas principales para buscar a partir de ellas
    query=query,                                            # ¿Qué estamos buscando?
    limit=limit)
    resp = requests.get(url=url, params=params)             # Buscar en la url definida con los parámetros elegidos
    name_database = json.loads(resp.text)                   # Convertirlo en un json y convertir la búsqueda en texto

    return name_database


##### FUNCIÓN 2: OBTENER LOS DATOS Y ORDENARLOS #####

def obtener_datos(bbdd,n):
    
    names = []
    lat = []
    long = []
   
    for i in range(n):
          
        names.append(bbdd["response"]["groups"][0]["items"][i]["venue"]["name"])
        lat.append(bbdd["response"]["groups"][0]["items"][i]["venue"]["location"]["lat"])
        long.append(bbdd["response"]["groups"][0]["items"][i]["venue"]["location"]["lng"])
        
    return names,lat,long


##### FUNCIÓN 3: CREAR DATAFRAME, AÑADIR IDENTIFICADOR Y GENERAR .CSV #####

def dataFrame_creation(nombre_dataframe, identificador):
    nombre_final = datos

    nombre_final = list(nombre_final)

    d = {"Identificador": identificador,"Nombre": nombre_final[0], "Latitud": nombre_final[1], "Longitud": nombre_final[2]}
    final = pd.DataFrame(data=d)

    final.to_csv(f"{nombre_dataframe}.csv")