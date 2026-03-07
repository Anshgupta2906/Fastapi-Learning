from fastapi import FastAPI
from fastapi.params import Body  

app = FastAPI()


@app.get("/")
def read_root():
    return {"Message": " hello my bestfriend!!!!!!!!!"}

@app.get("/posts")
def get_post():
    return{"data":"this is your post"}

@app.post("/createpost")
def create_post(payLoad:dict = Body(...)):
    print(payLoad)
    return{"new posts":f"title{payLoad['title']} content:{payLoad['content']}"}



