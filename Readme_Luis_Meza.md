En este escrito se describe los pasos de como se creo el api y los outputs solicitados por el proyecto.

## el archivo main.py:
En este archivo se codifica la api y los routers a aplicar(router1,router2,router3,router4,router5) del archivo routers.my_modules.

## el archivo requirements.txt:
contiene las versiones de los modulos a usar
* fastapi== 0.109.2
* pandas==2.1.0
* uvicorn==0.27.0.post1
* pyarrow == 15.0.0
* fastparquet==2024.2.0
* gunicorn== 21.2.0

## el archivo functions.py:
* Contiene las funciones a usar en los routers.
* El cargar los datos
1. df_1 = pd.read_parquet(r'./Data/Data_playtimegender.parquet')#T1
2. df_2= pd.read_parquet(r'./Data/UserForGender.parquet')#t2
3. df_3= pd.read_parquet(r'./Data/UsersRecommend.parquet')#T3
4. df_4 = pd.read_parquet(r'./Data/UsersRecommenT4.parquet')#T4 
5. df_master= pd.read_parquet(r'./Data/sentiment_analysis.parquet')#T5

### def PlayTimeGenre( genero : str ):
1. se recibe un texto
2. para evitar errores de mayusculas, todo se hizo mayusculas
3. se extrae la parte del genero elegido del df_1
4. Encontrar el año con el mayor valor acumulado de playtime_forever
5. se retorna un diccionario como resultado

### def UserForGenre( genero : str ):
1. se recibe un texto
2. para evitar errores de mayusculas, todo se hizo mayusculas
3. se extrae la parte del genero elegido del df_2
4. Se agrupa por 'user_id' y se suman los valores de 'playtime_forever'
5. se extrae el acumulado mayor.
6. se crea una variable para el la key del diccionario.
7. se retorna un diccionario como resultado indicando el usuario y las horas por año.

### def UsersRecommend( ano : int ):
1. se recibe un integral
2. se extrae la parte del año elegido del df_3 a un dataframe 'df_ano'.
3. se complementa con lineas vacias si el dataframe 'df_ano' no contiene 3 lineas.
4. df_ano se convierte en diccionario
5. se extrae el nombre de los  primeros 3 puestos de 'item_name' en df_ano en variables individuales
6. se retorna un diccionario con los 3 puestos y sus respectivos 'item_name'

### def UsersWorstDeveloper(año : int):
1. se recibe un integral
2. se extrae la parte del año elegido del df_3 a un dataframe 'df_ano2'.
3. se complementa con lineas vacias si el dataframe 'df_ano' no contiene 3 lineas.
4. df_ano se convierte en diccionario
5. se extrae el nombre de los  primeros 3 puestos de 'developer' en df_ano en variables individuales
6. se retorna un diccionario con los 3 puestos y sus respectivos 'developer'

### def sentiment_analysis( empresa_desarrolladora : str ): 
1. se recibe un texto
2. para evitar errores de mayusculas, todo se hizo mayusculas
3. se extrae la parte del 'developer' elegido del 'df_master'
4. se retorna un diccionario como resultado


# Carpeta de data:
se encuentran 5 archivos que son la base de datos para cada funcion:
1. Data_playtimegender.parquet
2. UserForGender.parquet
3. UsersRecommend.parquet
4. UsersRecommenT4.parquet
5. sentiment_analysis.parquet

# Carpeta routers:
## archivo my_modules.py:
1. se importan las librerias  APIRouter,JSONResponse,pandas   y las funciones de PlayTimeGenre, UserForGenre, UsersRecommend, UsersWorstDeveloper, sentiment_analysis.
2. se declaran los routers del 1 al 5:
    1. router1 = APIRouter() para  la funcion PlayTimeGenre
    2. router2 = APIRouter() para  la funcion UserForGenre
    3. router3 = APIRouter() para  la funcion UsersRecommen
    4. router4 = APIRouter() para  la funcion UsersWorstDeveloper
    5. router5 = APIRouter() para  la funcion sentiment_analysis
  
