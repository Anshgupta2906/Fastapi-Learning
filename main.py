from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Message": " hello my bestfriend!!!!!!"}

@app.get("/posts")
def get_post():
    return{"data":"this is your post"}