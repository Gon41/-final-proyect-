# IronHack Final Project - APP for accommodation in Madrid

## 1. Objective of the project

You are passionate about architecture and the history of cities. Whenever you can you become a tourist in another city. 

You have 3 days of vacation and you want to visit Madrid for the first time.

This application allows you while looking for accommodation to see what elements of interest both conventional (metro stops, art and history museums) and unconventional (outdoor art, palaces, ...) you can find in the radius of km you choose.

---------------------------------

![](https://www.soy-de.com/images/thumbs/%c2%bfCu%c3%a1ndo-reabrir%c3%a1-la-estaci%c3%b3n-de-Metro-de-Gran-V%c3%ada-0040047.jpeg)

---------------------------------

## 2. Data collection

The data have been obtained from two different sources:

------



### 2.1. Foursquare API

The service provided by the Foursquare API when called is to return data about the parameters we have passed (coordinates, update date, radius, search object and search limit).

-In the **2_Sacar_BBDD** file I have created a series of functions with the objective of obtaining information by passing the parameters I need,

    - Function 1: Make the API call
    - Function 2: Clean the result of the Function 1 and order
    - Function 3: Create a dataFrame with the data from Function 2, add an identifier for the category and generate a .cs for each API request.

--In the **3_Clean_Unite_BBDD** file I have revised cleaned and concatenated all the DBs by resetting the index.





----

### 2.2. AirBnB data

The airbnb data is not public, in fact there is an API to which they do not provide access unless you are an apartment owner.

However, they have been obtained through the page http://insideairbnb.com/ in the form of .csv.

Madrid is divided into 21 districts.

![](https://i.pinimg.com/564x/01/49/e3/0149e31c7d2d025e8d486d1a4eec17b7.jpg)


In the **4.AirBnB** file I have organized the dataset and generated three functions:

    - Function 4: Passes filters to the obtained .csv and returns a list of airbnb with the filters, allowing to discard those that do not meet them.
    - Function 5: From the list obtained with all the Foursquare data it obtains the distance to the coordinates of the airbnb we have chosen.
    - Function 6: Normalizes all the strings of the column name, eliminating tildes, dieresis, ñ, ...

----

In the following function files (AIRBNB, API and MAP) are the functions to be imported directly into the Jupyter Notebook.

    When importing the **FINAL_functions** file, just by entering the code **airbnb_final()** you start generating the complete program.

    It asks you a series of questions about the District, type of accommodation, price range, minimum nights of accommodation, minimum reviews, maximum radius (in km) and how many identifiers of each type you want it to display.

    You get a list of airbnbs with those characteristics, and it asks you to enter the id of the chosen airbnb, to get as an end point the map.

![Optional Text](../-final-proyect-/images/foto_fin.png)
 

