    #importar libreria
import pandas as pd
import os
#cargo de datos
df_1 = pd.read_parquet(r'./Data/Data_playtimegender.parquet')#T1
df_2= pd.read_parquet(r'./Data/UserForGender.parquet')#t2
df_3= pd.read_parquet(r'./Data/UsersRecommend.parquet')#T3

df_master= pd.read_parquet(r'./Data/sentiment_analysis.parquet')#T5

#T1 UserForGender

def PlayTimeGenre( genero : str ):
    genero = genero.upper() #para evitar errores de mayusculas, todo se hizo mayusculas

    #revisar que el genero si sea un str y que este dentro del listado de generos posibles
    if genero not in df_1['genres'].unique():
        raise ValueError(f"El género '{genero}' no se encuentra en la base de datos favor de verificarlo.")
    
   
    df_query = df_1[df_1['genres'] == genero] #se extrae la parte del genero elegido

    # Encontrar el año con el mayor valor acumulado de playtime_forever
    df_query=df_query.sort_values(by='playtime_forever', ascending=False)
    resultado = df_query['release_date'].iloc[0]
    dic = {f'Año de lanzamiento con más horas jugadas para Género {genero}' : resultado.tolist()}
    return dic

#T2 UserForGenre
def UserForGenre( genero : str ):
    # verificar que sea  str y cambiarlo a mayusculas para evitar errores
    genero = genero.upper() #para evitar errores de mayusculas, todo se hizo mayusculas

    #revisar que el genero si sea un str y que este dentro del listado de generos posibles
    if genero not in df_2['genres'].unique():
        raise ValueError(f"El género '{genre}' no se encuentra en la base de datos favor de verificarlo.")

    #buscar al mas perron y sus años
    df_action = df_2[df_2['genres'] == genero]
    acumulado_por_usuario = df_action.groupby('user_id')['playtime_forever'].sum()
    usuariomax = acumulado_por_usuario.idxmax()
    
    
    acumulado_por_usuario_fecha = df_action.groupby(['user_id', 'release_date'])['playtime_forever'].sum()
    
    dic= {'Usuario con más horas jugadas para Género {genero}' : usuariomax, "Horas jugadas: ": acumulado_por_usuario_fecha[usuariomax].to_dict()}

    return dic
    

#T3  UsersRecommend
def UsersRecommend( ano : int ): 
    
    ######verificar que este el año pedido ente los datos
    '''
    if year not in df_3['release_date'].unique() or type(year) != int :
        raise ValueError(f"El género '{year}' no se encuentra en la base de datos favor de verificarlo.")
    '''
    ## extraer los datos del ano
    df_ano= df_3[df_3['release_date']==ano]
    df_ano.to_dict(orient='records') # convertir en dictionary para ser usado en json
    '''if df_ano.size >8:
        p1=df_ano['item_name'].iloc[0]
        p2= df_ano.get(['item_name']).iloc[1]
        p3=df_ano.get(['item_name']).iloc[2]
    elif df_ano.size <4 :
        p1=df_ano['item_name'].iloc[0]
        p2= "no hay"
        p3= "no hay"
    else:
        p1=df_ano['item_name'].iloc[0]
        p2= df_ano.get(['item_name']).iloc[1]
        p3= "no hay"
    '''
    p1=df_ano['item_name'].iloc[0]
    p2= df_ano.get(['item_name']).iloc[1]
    p3=df_ano.get(['item_name']).iloc[2]
    return {"Puesto 1" :p1 , "Puesto 2" : p2,"Puesto 3" : p3}
    
        
#T4 UsersWorstDeveloper
df_4 = pd.read_parquet(r'./Data/UsersRecommenT4.parquet')#T4  
def UsersWorstDeveloper(año : int):
    
    df_ano2 = df_4[df_4['release_date']==año]
    df_ano2.to_dict(orient='records') # convertir en dictionary para ser usado en json

    if df_ano2.size >7:
        return {"Puesto 1" :df_ano2['developer'].iloc[0] , "Puesto 2" : df_ano2['developer'].iloc[1],"Puesto 3" : df_ano2['developer'].iloc[2]}
    elif df_ano2.size <4:
         return {"Puesto 1" :df_ano2['developer'].iloc[0] , "Puesto 2" : "no hay","Puesto 3" :  "no hay"}
    else:
        return {"Puesto 1" : df_ano2['developer'].iloc[0]}, "Puesto 2" : df_ano2['developer'].iloc[1],"Puesto 3" : "no hay"}
   
    
    

#T5 empresa_desarrolladora
def sentiment_analysis( empresa_desarrolladora : str ): 
    
    empresa_desarrolladora = empresa_desarrolladora.upper() #para evitar errores de mayusculas, todo se hizo mayusculas

    #revisar que el genero si sea un str y que este dentro del listado de generos posibles
    if empresa_desarrolladora not in df_master['developer'].unique():
        raise ValueError(f"El Desarrollador '{empresa_desarrolladora}' no se encuentra en la base de datos favor de verificarlo.")

    dev = df_master[df_master['developer'] == empresa_desarrolladora]
    #lista=  {'Negative': dev['negativo'].iloc[0], 'Neutral= ': dev['neutro'].iloc[0], 'Positive=': dev['positivo'].iloc[0]}

    dicc ={empresa_desarrolladora: {'Negative': int(dev['negativo'].iloc[0]), 'Neutral= ': int(dev['neutro'].iloc[0]), 'Positive=': int(dev['positivo'].iloc[0])}}
    return dicc
  
