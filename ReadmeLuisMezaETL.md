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
1. se cargan los archivos json nombrados Clean_DataGames.json y Clean_Players.json.
2. Se mezclan mediante la columna 'item_id'.
3. Un nuevo DF donde la mezcla se le agrupa por 'genres', 'release_date' y se suman los valores de playtime_forever.
4. se guarda este nuevo DF como 'Data_playtimegender.parquet' para mejorar la carga del api.
5. Se crea el prototipo de funcion para la consigna de obtener el Año de lanzamiento con más horas jugadas para Género elegido.

### archivo 'UserForGender.ipynb'
se cargan los archivos json nombrados Clean_DataGames.json y Clean_Players_T2.json.
1. Se mezclan mediante la columna 'item_id'.
2. Se eliminan las columnas innecesarias 'item_id',	'developer'.
3. Convertir a mayusculas los valores de 'user_id'. 
4. Se crea el prototipo de funcion para la consigna de obtener al "Usuario con más horas jugadas para Género " ,genero elegido,' y las "Horas jugadas:" por cada año.


### archivo 'UsersRecommend.ipynb'
se cargan los archivos json nombrados Clean_DataGames_T3.json y Clean_GamesRev.json.
1. Se mezclan mediante iguales.
2. Se crea la funcion 'analyze_sentiment' para analizar los comentarios  usando variables con un listado de palabras clave para saber si es un comentario positivo y otra para para identificar los comentarios negativos y dar un resultado en valor int.
3. Se agrega la columna 'sentiment_analysis' llenadola con el resultado de aplicar la funcion 'analyze_sentiment' en los valores de la columna 'review'.
4. Se analiza cual es el idioma en el que estan escritos los comentarios para identificar el mas reelevante. english 39016
5. Se agrega 1 punto al 'sentiment_analysis' si ['recommend'] == True, y se quita 1 punto si es False.
6. Se crea la tabla 'Clean_GamesRevT5.json' que sera usada en T5sentimen_analysis.ipynb
7. Se agrupa ['item_id','item_name','release_date'] y se suman los valores de['sentiment_analysis'] en un dataframe.
8. Se separa los ['sentiment_analysis'] los positivos en un dataframe df_t3.
9. Se separa los ['sentiment_analysis'] los negativos en un dataframe df_t4 y se guarda como 'UsersRecommendNeg.parquet'
10. El df_t3 es ordenado en descendente por los valores de 'release_date', 'sentiment_analysis'.
11. Se guardan los valores de las columnas item_name	release_date de "df_t3" en "top_3_per_year".
12. DataFrame "top_3_per_year"  se guarda como 'UsersRecommend.parquet'
13. Se crea el prototipo de funcion para la consigna del top 3 de juegos MÁS recomendados por usuarios para el año dado.

### archivo 'UserWorstDeveloper.ipynb'
1. Se carga 'UsersRecommendNeg.parquet' en un dataframe 'd_Reviews'
2. Se carga 'Clean_DataGames.json' y extrae ['item_id', 'developer'] en un dataframe 'D_dev'
3. Se mezclan(merge) por la columna de 'item_id'
4. Se agrupan por el top3 de'release_date'. y se ordenan 'release_date', 'sentiment_analysis' en descenso en el dataframe "top_3_per_year".
5. A "top_3_per_year" se elimina la columna 'sentiment_analysis'.
6. Se guarda la base de datos como 'UsersRecommenT4.parquet'.
7. Se crea el prototipo de funcion para la consigna de el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado.

### archivo 'sentiment_analysis.ipynb'
1. Se carga 'Clean_DataGames.json' y extrae ['item_id', 'developer'] en un dataframe 'D_dev'
2. Se carga 'Clean_GamesRevT5.json' en un dataframe 'df_rev'
3. Se crea una funcion 'categorize_sentiment' para categorizar si el comentario es positivo, negativo o neutro y agregarle un +1 a la columna de la categoria correspondiente.
4. Se aplica la funcion 'categorize_sentiment' en  df_rev.
5. Se eliminan las columanas de 'item_name','release_date','sentiment_analysis' de df_rev.
6. Se mezclan las columnas de df_dev, df_rev, por medio de la columna 'item_id'.
7. Se agrupa por 'developer' y se suman los valores de las columnas positivo	neutro	negativo
8. De esta tabla se tira la columna de item_id
9. Se guarda como 'sentiment_analysis.parquet'.
10. Se crea el prototipo de funcion para la consigna de el registro del sentiment analysis para un desarrollador.


### archivo recomendacion_juego.ipynb
1. Filtrar el DataFrame para obtener solo las filas correspondientes al item_id de consulta
2. Calcular la similitud de coseno entre el item de consulta y todos los demás items
3. Obtener los índices de los items más similares (excepto el item de consulta)
4. Obtener los nombres de los items más similares
5. crear la llave para el diccionario
6. Mostrar los nombres de los items más similares




