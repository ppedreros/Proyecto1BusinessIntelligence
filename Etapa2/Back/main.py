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
    df = pd.DataFrame(dataModel.Review, columns=dataModel.columns())
    print(df)
    model = load("assets/modelo.joblib") 
    print(model)
    df["Class"] = model.predict(df["Review"])
    print(df)
    return df.to_dict()

