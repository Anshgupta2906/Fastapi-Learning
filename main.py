from fastapi import FastAPI
from fastapi.params import Body  
from pydantic import BaseModel
from random import randrange

app = FastAPI()


class Client(BaseModel):
    name: str
    primary_goal: str
    body_weight:int
    published:bool= False

clients_db=[{"Name":"Name of the client", "Goal":"specific goal of client 1","id":1},
{"Name":"Ankit kumar","Goal":"Body recompositon","id":2}]

@app.get("/")
def read_root():
    return {"Message": " How are you feeling"}

@app.get("/goals")
def get_goals():
    return clients_db

@app.post("/clients")
def body_weigth(client:Client):
    new=client.dict()
    new['id'] = randrange(0,1000000)
    clients_db.append(new)
    return new

#title str,content str, category,bool published or draft


