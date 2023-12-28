from model import model_pipeline
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    content: str

app = FastAPI()

@app.post("/ask")
def ask(item: Item):
    query = item.content
    result = model_pipeline(query=query)
    return {"answer": result}