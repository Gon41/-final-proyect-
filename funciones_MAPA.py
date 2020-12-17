import pandas as pd
from folium.plugins import MeasureControl,MiniMap
from folium import Map, Marker, Icon, FeatureGroup, LayerControl, Choropleth
import folium


##### FUNCIÓN 7: CREAR MAPA #####

def pintar_mapa(lat,lon,distance,number):
    
    # Ejecuto el mapa
    
    map1 = folium.Map(location=(lat,lon),tiles='Stamen Terrain',zoom_start=13)    


    # Puntos fijos
    
    marker_puerta_sol = folium.Marker(location=(40.4146500,-3.7004000), popup="Puerta del Sol", tooltip="KM O", icon = folium.Icon(icon='flag', color= "black", prefix='fa')).add_to(map1)

    # Cargo el dataset
    
    data = pd.read_csv("KM.csv")
    
    # Museos de arte
    
    lst_coord = data.loc[((data["Identificador"] == "Museo de Arte") & (data["Distancia_km"] < distance))].sort_values("Distancia_km").nsmallest(number, 'Distancia_km')
    lst_lat = [lst_coord["Latitud"][i] for i in lst_coord.index]
    lst_lon = [lst_coord["Longitud"][i] for i in lst_coord.index]
    lst_nom = [lst_coord["Nombre"][i] for i in lst_coord.index]   
    
    museo_arte = FeatureGroup(name='Museo de Arte')
    
    for i in range(len(lst_lat)):
        coord = [lst_lat[i],lst_lon[i]]
        marker = folium.Marker(location=(coord), popup=lst_nom[i], tooltip="Museo de Arte", icon=folium.Icon(icon='paint-brush ', color= "green", prefix='fa')).add_to(map1)
        folium.Marker(location=(coord)).add_to(museo_arte)
        map1.add_child(museo_arte)
    
    # Esculturas al aire libre
    
    lst_coord = data.loc[((data["Identificador"] == "Escultura Exterior") & (data["Distancia_km"] < distance))].sort_values("Distancia_km").nsmallest(number, 'Distancia_km')
    lst_lat = [lst_coord["Latitud"][i] for i in lst_coord.index]
    lst_lon = [lst_coord["Longitud"][i] for i in lst_coord.index]
    lst_nom = [lst_coord["Nombre"][i] for i in lst_coord.index] 
    
    esculturas = FeatureGroup(name='Esculturas al aire libre')
    
    for i in range(len(lst_lat)):
        coord = [lst_lat[i],lst_lon[i]]
        marker = folium.Marker(location=(coord), popup=lst_nom[i], tooltip="Escultura al aire libre", icon = folium.Icon(icon='caret-up', color= "purple", prefix='fa')).add_to(map1)
        folium.Marker(location=(coord)).add_to(esculturas)
        map1.add_child(esculturas)
        
    # Campos de futbol
    
    lst_coord = data.loc[((data["Identificador"] == "Estadio de Fútbol") & (data["Distancia_km"] < distance))].sort_values("Distancia_km").nsmallest(number, 'Distancia_km')
    lst_lat = [lst_coord["Latitud"][i] for i in lst_coord.index]
    lst_lon = [lst_coord["Longitud"][i] for i in lst_coord.index]
    lst_nom = [lst_coord["Nombre"][i] for i in lst_coord.index]
    futbol = FeatureGroup(name='Campos de Fútbol')
    
    for i in range(len(lst_lat)):
        coord = [lst_lat[i],lst_lon[i]]
        marker = folium.Marker(location=(coord), popup=lst_nom[i], tooltip="Estadio de Futbol", icon = folium.Icon(icon='soccer-ball-o', color= "gray", prefix='fa')).add_to(map1)
        folium.Marker(location=(coord)).add_to(futbol)
        map1.add_child(futbol)
        
    # Museo de Historia
    
    lst_coord = data.loc[((data["Identificador"] == "Museo de Historia") & (data["Distancia_km"] < distance))].sort_values("Distancia_km").nsmallest(number, 'Distancia_km')
    lst_lat = [lst_coord["Latitud"][i] for i in lst_coord.index]
    lst_lon = [lst_coord["Longitud"][i] for i in lst_coord.index]
    lst_nom = [lst_coord["Nombre"][i] for i in lst_coord.index]
    museo_historia = FeatureGroup(name='Museos de Historia')
    
    for i in range(len(lst_lat)):
        coord = [lst_lat[i],lst_lon[i]]
        marker = folium.Marker(location=(coord), popup=lst_nom[i], tooltip="Museo de Historia", icon = folium.Icon(icon='institution', color= "cadetblue", prefix='fa')).add_to(map1)
        folium.Marker(location=(coord)).add_to(museo_historia)
        map1.add_child(museo_historia)
        
    # Palacio
    
    lst_coord = data.loc[((data["Identificador"] == "Palacio") & (data["Distancia_km"] < distance))].sort_values("Distancia_km").nsmallest(number, 'Distancia_km')
    lst_lat = [lst_coord["Latitud"][i] for i in lst_coord.index]
    lst_lon = [lst_coord["Longitud"][i] for i in lst_coord.index]
    lst_nom = [lst_coord["Nombre"][i] for i in lst_coord.index]
    
    palacios = FeatureGroup(name='Palacios')
    
    for i in range(len(lst_lat)):
        coord = [lst_lat[i],lst_lon[i]]
        marker = folium.Marker(location=(coord), popup=lst_nom[i], tooltip="Palacio", icon = folium.Icon(icon='fort-awesome', color= "beige", prefix='fa')).add_to(map1)
        folium.Marker(location=(coord)).add_to(palacios)
        map1.add_child(palacios)
        
    # Metro
    
    lst_coord = data.loc[((data["Identificador"] == "Metro Station") & (data["Distancia_km"] < distance))].sort_values("Distancia_km").nsmallest(number, 'Distancia_km')
    lst_lat = [lst_coord["Latitud"][i] for i in lst_coord.index]
    lst_lon = [lst_coord["Longitud"][i] for i in lst_coord.index]
    lst_nom = [lst_coord["Nombre"][i] for i in lst_coord.index]
    
    metro = FeatureGroup(name='Paradas de Metro')
    
    for i in range(len(lst_lat)):
        coord = [lst_lat[i],lst_lon[i]]
        marker = folium.Marker(location=(coord), popup=lst_nom[i], tooltip="Parada de Metro", icon = folium.Icon(icon='subway', color= "orange", prefix='fa')).add_to(map1)
        folium.Marker(location=(coord)).add_to(metro)
        map1.add_child(metro)
        
     
    # Otros Airbnb cercanos
        
    pisos_elegidos = pd.read_csv("Pisos_elegidos.csv")
    
    lst_lat = [pisos_elegidos["latitude"][i] for i in pisos_elegidos.index]
    lst_lon = [pisos_elegidos["longitude"][i] for i in pisos_elegidos.index]
    
    pisos_elegidos = FeatureGroup(name='Otros AirBnB')

    no_pintar = lat,lon
    
    for i in range(len(lst_lat)):

        coord = [lst_lat[i],lst_lon[i]]
        marker = folium.Marker(location=(coord),tooltip="AriBnB Alternativo").add_to(map1)
        folium.Marker(location=(coord)).add_to(pisos_elegidos)
        map1.add_child(pisos_elegidos)

        # Airbnb
    
    marker_airbnb = folium.Marker(location=(lat,lon), popup="AirBnB", tooltip="Ubicacion AirBnB", icon = folium.Icon(icon='home', color= "red", prefix='fa')).add_to(map1)   

    
        
    ## Pluggins
    
    # Agrego un medidor de distancias (seleccionas dos puntos y te dice la distancia entre medias)


    map1.add_child(MeasureControl())

    # Agrego un indicador de con cada click indica las coordenadas de ese punto

    map1.add_child(folium.LatLngPopup())
    
    # Añadir el filtro para poder seleccionar lo que deseas
    
    map1.add_child(folium.map.LayerControl())
    
    # Añadir minimapa
    
    minimap = MiniMap(toggle_display=True)
    minimap.add_to(map1)

    return map1