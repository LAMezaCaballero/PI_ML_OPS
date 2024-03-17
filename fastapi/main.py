from fastapi import FastAPI, routing

from fastapi.responses import JSONResponse
from routers.my_modules import router1,router2,router3,router4,router5


app=FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hola Mundo"}

app.include_router(router1)
app.include_router(router2)
app.include_router(router3)
app.include_router(router4)
app.include_router(router5)

