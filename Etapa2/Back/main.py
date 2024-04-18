from typing import Optional
import pandas as pd
from fastapi import FastAPI
from joblib import load
from dataModel import DataModel
import preprocessing as pp

app = FastAPI()

@app.get("/")
def read_root():
   return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
   return {"item_id": item_id, "q": q}

@app.post("/predict")
def make_predictions(dataModel: DataModel):
    print(dataModel.dict())
    df = pd.DataFrame(dataModel.dict(), columns=dataModel.dict().keys(), index=[0])
    df.columns = dataModel.columns()
    model = load("modelo.joblib") ##Model.joblib fallando, estamos haciendo mal el pipeline.
    result = model.predict(df)
    return result ## Falta ver si este return es diferente por ser un resultado numerico aca o en predictionModel
