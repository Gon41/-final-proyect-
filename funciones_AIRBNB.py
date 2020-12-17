import pandas as pd
import numpy as np
import re
from unicodedata import normalize
from haversine import haversine, Unit
           


##### FUNCIÓN 4: BÚSQUEDA DE PISOS #####


def busquedas_piso(distrito, kind, min_price, max_price, minimum_nights,number_reviews):


    data = pd.read_csv("listings.csv")
    # Filtros
    lst_pisos = data.loc[((data["neighbourhood_group"] == distrito) & (data["room_type"] == kind) & ((data["price"] > min_price) 
                        & (data["price"] < max_price)) & (data["minimum_nights"] == minimum_nights) & (data["number_of_reviews"] > number_reviews))]
    
    # Ordenar en función del precio (ascendente) y la cantidad de reseñas
    lst_pisos = lst_pisos.sort_values(['price', 'number_of_reviews'], ascending=[True, False])
    
    lst_pisos = lst_pisos.drop(columns=["Unnamed: 0"])



    if len(lst_pisos) > 0:

        display(lst_pisos)
        
        lst_pisos.to_csv("Pisos_elegidos.csv")
    
        return 1
    
    elif len(lst_pisos) <= 0:
        print("No se ha encontrado resultados con esos requisitos. Varie algún parámetro")

        return 0 
    


##### FUNCIÓN 5: CALCULAR DISTANCIAS #####

def calcular_km(lat_airbnb,lon_airbnb):

    data = pd.read_csv("DataFrame_Parametros.csv")        # Abro el CSV con la base de datos

    airbnb = (lat_airbnb,lon_airbnb)

    lst_lat = [data["Latitud"][i] for i in data.index]    # Hago una lista de las latitudes del CSV
    lst_lon = [data["Longitud"][i] for i in data.index]   # Hago una lista de las longitudes del CSV

    tuples = [tupla for tupla in zip(lst_lat,lst_lon)]    # Hago una lista de tuplas con las dos listas anteriores
                                                          # La función zip devuelve un iterador de tuplas
        
    tup = [haversine(airbnb,coord) for coord in tuples]   # Calculo la distancia con haversine, identando por las coordinadas
    
    data["Distancia_km"] = tup                            # Creo la columna "Distancia_km" en data
    
    data.to_csv("KM.csv")                                 # Exportar
    
    return "Columna sacada con éxito"


##### FUNCIÓN 6: NORMALIZAR NOMBRE #####

def normalizar():

    data_km = pd.read_csv("KM.csv")
    lst_nombres = [data_km["Nombre"][i] for i in data_km.index]

    lista_normalizada = []

    for i in lst_nombres:

        i = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
                    normalize( "NFD", i), 0, re.I)

        i = normalize( 'NFC', i)

        lista_normalizada.append(i)

    return lista_normalizada