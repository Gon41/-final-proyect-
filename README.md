# Proyecto Final IronHack - APP de alojamiento en Madrid

## 1. Objetivo del proyecto

Quieres ir a visitar una ciudad desconocida y entre las múltiples posibilidades de alojamiento ¿cuál eliges?.

El fin de esta APP es dar un mapa de localizaciones importantes como paradas de metro, museos de arte e historia, arte al aire libre, palacios, ... Todo aquello que haga de tu llegada a la casa un museo viviente.

---------------------------------
<img src="../-final-proyect-/metro.jpeg">

---------------------------------

## 2. Obtención de los datos

Los datos han sido obtenidos de dos fuentes diferentes:

------


### 2.1. API Foursquare

El servicio que presta la API de Foursquare al ser llamada es devolver datos acerca de los parámetros que hemos pasado(coordenadas,fecha de actualización, radio, objeto de búsqueda y limite de búsquedas)

-En el archivo **2_Sacar_BBDD** he creado una serie de funciones con el objetivo de obtener información pasando los parámetros que necesito,

    - Función 1: Hacer la llamada a la API
    - Función 2: Limpiar el resultado de la Función 1 y ordenar
    - Función 3: Crear un dataFrame con los datos de la Función 2, añadir un identificador para la categoría y generar un .cs para cada petición a la API.

--En el archivo **3_Limpiar_Unir_BBDD** he revisado limpiado y concatenado todas las BBDD reseteando el índice.



----

### 2.2. Datos de AirBnB

Los datos de los airbnbs no son públicos, de hecho existe una API a la que no proporcionan acceso a menos que seas un propietario de un piso.

Sin embargo, han sido obtenidos a través de la página http://insideairbnb.com/ en forma de .csv.

Madrid se divide en 21 distritos.

<img src="../-final-proyect-/portada.jpg">

En el archivo **4.AirBnB** he organizado el dataset y he generado tres funciones:

    - Función 4: Pasa filtros al .csv obtenido y devuelve una lista de airbnb con los filtros, permitiendo descartar los que no  los cumplen.
    - Función 5: De la lista obtenida con todos los datos de Foursquare obtiene la distancia a los que se encuentran de las coordenadas del airbnb que hemos elejido.
    - Función 6: Normaliza todos los strings de la columna nombre, elminando tildes, dieresis, ñ, ...

----

En los sucesivos archivos de funciones(AIRBNB,API y MAPA) se encuentran las funciones para ser importadas directamente en el Jupyter Notebook.

    Al importar el archivo de **funciones_FINAL** solo con introducir el código **airbnb_final()** se empieza a generar el programa completo.

    Te hace una serie de preguntas sobre el Distrito, tipo de alojamiento, intervalo de precio,  minimo de noches de alojamiento, minimo de reseñas, radio máximo (en km) y cuantos identificadores de cada tipo deseas que muestre.

    Obtienes una lista de airbnbs con esas caracteristicas, y te pide introducir el id del airbnb elegido, para obtener como punto final el mapa.

<img src="../-final-proyect-/foto_fin.png">
 

