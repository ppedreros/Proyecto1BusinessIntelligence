from io import BytesIO
from typing import Optional
import pandas as pd
from fastapi import FastAPI, File, UploadFile
from joblib import load
from dataModel import DataModel
import preprocessing as pp
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configurar los orígenes permitidos
origins = [
    "http://localhost",
    "http://localhost:3000",  # Aquí debes incluir la URL de tu aplicación React
]

# Configurar middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
   return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
   return {"item_id": item_id, "q": q}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    # Aquí puedes procesar los contenidos del archivo CSV (contents)
    # Por ejemplo, puedes guardarlos en una base de datos o procesarlos de alguna manera.
    return {"filename": file.filename}

# Define el endpoint para recibir el archivo CSV y realizar predicciones
@app.post("/predict")
async def make_predictions(file: UploadFile = File(...)):
   # Lee el contenido del archivo CSV y crea un DataFrame
   contents = await file.read()
   # Crea un objeto BytesIO a partir de los bytes
   bytes_io = BytesIO(contents)

   # Lee el contenido del archivo CSV y crea un DataFrame
   df = pd.read_csv(bytes_io)
   model = load("assets/modelo.joblib") 
   # Realiza las predicciones con el modelo cargado
   df["Class"] = model.predict(df["Review"])

   # Devuelve los resultados como un diccionario
   return df.to_dict()

