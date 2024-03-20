from fastapi import APIRouter
from fastapi.responses import JSONResponse
from functions import PlayTimeGenre, UserForGenre, UsersRecommend, UsersWorstDeveloper, sentiment_analysis, recomendacion_juego
import pandas as pd

router1 = APIRouter()
router2 = APIRouter()
router3 = APIRouter()
router4 = APIRouter()
router5 = APIRouter()
router6 = APIRouter()

@router1.get("/PlayTimeGenre/{genero}")
def read_PlayTimeGenre(genero: str):
    result = PlayTimeGenre(genero)
    return JSONResponse(content=result)

@router2.get("/UserForGenre/{genero}")
def read_UserForGenre(genero: str):
    result = UserForGenre(genero)
    return JSONResponse(content=result)

@router3.get("/UsersRecommend/{año}")
def read_UsersRecommend(year: int):
    result = UsersRecommend(year)
    return JSONResponse(content=result)

@router4.get("/UsersWorstDeveloper/{año}")
def read_UsersWorstDeveloper(year: int):
    result = UsersWorstDeveloper(year)
    return JSONResponse(content=result)

@router5.get("/sentiment_analysis/{empresa_desarrolladora}")
def read_sentiment_analysis(empresa_desarrolladora : str):
    result = sentiment_analysis(empresa_desarrolladora)
    return JSONResponse(content=result)

@router6.get("/recomendacion_juego/{item_id}")
async def read_recomendacion_juego(juego : int):
    result = recomendacion_juego(juego)
    return JSONResponse(content=result)
