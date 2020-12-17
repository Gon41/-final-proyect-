import pandas as pd
import re
from unicodedata import normalize
from haversine import haversine, Unit 
import folium
from folium.plugins import MeasureControl,MiniMap
from folium import Map, Marker, Icon, FeatureGroup, LayerControl, Choropleth


from funciones_AIRBNB import busquedas_piso,calcular_km,normalizar
from funciones_MAPA import pintar_mapa


def airbnb_final():
    
    distrito = str(input("Introduce el distrito de Madrid dónde quieres alojarte: "))
    kind = str(input("¿Qué tipo de alojamiento deseas? (Entire home/apt, Private room, Shared room o Hotel room): "))
    min_price = int(input("Introduce el mínimo precio que estás dispuesto a pagar: "))
    max_price = int(input("Introduce el máximo precio que estás dispuesto a pagar: "))
    minimum_nights = int(input("Introduce el mínimo de noches que quieres alojarte: "))
    number_reviews = int(input("Introduce el mínimo de reseñas que quieras que tenga el anuncio del alojamiento: "))
    distance = int(input("¿Qué radio máximo (en km) quieres ver: "))
    number = int(input("¿Cuántos identificadores como máximo quieres ver de cada tipo: "))
                         
    pisos = busquedas_piso(distrito, kind, min_price, max_price, minimum_nights,number_reviews)
    
    while pisos == 0:
        
        break
    
    else:

        data = pd.read_csv("Pisos_elegidos.csv")

        id_airbnb = int(input("Introduce el ID del airbnb seleccionado: "))

        lst_coord = data.loc[((data["id"] == id_airbnb))]
        lat,lon = lst_coord["latitude"],lst_coord["longitude"]



        calcular_km(lat,lon)

        normalizar()

        return pintar_mapa(lat,lon,distance,number)