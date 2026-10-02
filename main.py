from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    age: int


@app.get("/")
def home():
    return {
        "message": "Hello AI World 🚀"
    }


@app.get("/hello")
def hello():
    return {
        "message": "Hello Waris! Welcome to AI Engineering 🚀"
    }


@app.post("/user")
def create_user(user: User):
    return {
        "message": f"Hello {user.name}",
        "age": user.age
    }
    
@app.get("/about")
def about():
    return {
        "name": "Waris",
        "role": "AI Engineer",
        "goal": "Build AI products"
}