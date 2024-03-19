# proceso de Extract Transform Load

## EXTRACCION

Los archivos que estan en formato json.gz dados en por el cliente se descomprimieron para poder abrirlos, revisarlos y transformarlos para tenerlos disponibles para las consignas.

### archivo 'output_steam_games.json'
#### Primera observacion
* cientos de lineas vacias.
* columnas app_name	y title	 tienen casi los mismos datos por lo que nos quedaremos con app_name.
* columna genres tiene un listado
* release_date tiene diferentes formatos de fechas y algunos valores vacios.

### Todas esto sera corregido en el archivo "etl_games.ipynb" 
#### Cambios a estos datos para la consigna de 'PlayTimeGenre'. 
Para la primer consigna se extraen las columnas (genres,  release_date,	id, developer) las cuales se limpian de los vacios individuales.
1. release_date: se estandariza el formato de la columna, y despues se extrae solo el ano.
2. genres: se expande la lista para que cada elemento de cada lista tenga su propia linea.
3. formato y tipo de datos: si es str el valor se convierte en mayusculas, release_date se convierte en int y se cabia el nombre de la columna id a item_id.
4. Se guarda este Dataframe como  'Clean_DataGames.json'

#### Cambios a estos datos para la consigna de 'UserRecommend'. 
Para la tercer consigna se extraen las columnas (item_name,	release_date,	item_id) las cuales se limpian de los vacios individuales.
1. release_date: se estandariza el formato de la columna, y despues se extrae solo el ano.
2. genres: se expande la lista para que cada elemento de cada lista tenga su propia linea.
3. formato y tipo de datos: si es str el valor se convierte en mayusculas, release_date se convierte en int y se cabia el nombre de la columna id a item_id.
4. Se guarda este Dataframe como 'Clean_DataGames_T3.json'.

### archivo australian_user_reviews.json
#### Primera observacion:
*   user_id tiene valores.
*   reviews tiene anidado muchos diccionarios para cada linea
*   los diccionarios tienen el item_id, recommend y review.

#### Estos datos seran trabajan en el archivo "etl_Games_rev.ipynb"
1. Se carga el archivo en un df.
2. Reviews se desanida cada diccionario leyendo cada linea con agregando en un listado vacio.
3. se concatena en si mismo para convertir la lista en dataframe 'df_rev'.
4. Extraemos item_id	recommend	review columnas de 'df_rev'.
5. Se guarda este DataFrame como  'Clean_DataGamesRev.json'.

### archivo australian_users_items.json
#### Primera observacion:
*   Tiene errores de edicion en la comilla simple en vez de doble.
*   El item_id, item_name y playtime_forevers estan anidados en un diccionario por linea de jugador.
*   playtime_forever esta medido en minutos.
*   no tienen elementos vacios.

#### Estos datos seran trabajan en el archivo "etl_Players.ipynb"
1. Se carga el archivo en un df, corrigiendo la edicion json.
2.  aqui se divide para la consigna de 'PlayTimeGenre' o brincar a 'UserforGender'.
   
#### Cambios a estos datos para la consigna de 'PlayTimeGenre'
1. Reviews se desanida cada diccionario leyendo cada linea con agregando en un listado vacio.
2. Se concatena en si mismo para convertir la lista en dataframe 'data_items_horas'.
3. Extraemos item_id	item_name	playtime_forever de 'data_items_horas'.
4. Convertimos playtime_forever en int, a horas y eliminar los que sean 0 horas.
5. Eliminamos los valores vacios, cambiamos item_name a mayusculas.
6. se agrupan los valores por item_id y se suman playtime_forever, guardando en un nuevo DF
7. se mezclan(merge) el Df principal con el nuevo DF
8. Se guarda esta mezcla como  'Clean_Players.json'.

#### Cambios a estos datos para la consigna de 'UserforGender'
1. Reviews se desanida cada diccionario leyendo cada linea con agregando en un listado vacio.
2. Se concatena en si mismo para convertir la lista en dataframe 'data_items_horas'
3. Normalizar 'data_items_horas' con user_id
4. Extraer item_id	playtime_forever	user_id.
5. Convertimos playtime_forever en int, a horas y eliminar los que sean 0 horas.
6. Convertir item_id en mayusculas.
7. Se guarda esta mezcla como 'Clean_Players_T2.json'


## transformacion 
Se crea una tabla de datos para cada consigna, mezclando las tablas limpias del paso de extraccion.
### archivo 'PlayTimeGenre.ipynb'
1. se cargan los archivos json nombrados Clean_DataGames y Clean_Players.
2. Se mezclan mediante la columna 'item_id'.
3. Un nuevo DF donde la mezcla se le agrupa por 'genres', 'release_date' y se suman los valores de playtime_forever.
4. se guarda este nuevo DF como 'Data_playtimegender.parquet' para mejorar la carga del api.
5. Se crea la funcion para la consigna de obtener el Año de lanzamiento con más horas jugadas para Género elegido.


   




