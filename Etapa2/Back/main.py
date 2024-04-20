from io import BytesIO
from typing import Optional
import pandas as pd
from fastapi import FastAPI, File, UploadFile
from joblib import load
from dataModel import DataModel
import preprocessing as pp
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",  
]

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
   return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
   return {"item_id": item_id, "q": q}


@app.post("/predictCSV")
async def make_predictions(file: UploadFile = File(...)):
   contents = await file.read()
   bytes_io = BytesIO(contents)
   df = pd.read_csv(bytes_io)
   model = load("assets/modelo.joblib") 
   df["Class"] = model.predict(df["Review"])
   return df.to_dict()


class PredictionRequest(BaseModel):
    text: str

class PredictionResponse(BaseModel):
    predictions: dict

@app.post("/predictText", response_model=PredictionResponse)
async def make_predictionsText(request: PredictionRequest):
    df = pd.DataFrame({'Review': [request.text]})
    model = load("assets/modelo.joblib")
    prediction = model.predict(df["Review"])[0]  
    prediction = int(prediction)

    return {"predictions": {"Review": request.text, "Class": prediction}}


