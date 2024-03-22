from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return { "message": "Hello Root!" }

@app.get("/home")
def home():
    return { "message": "Home!" }

@app.get("/test")
def test():
    return "Here is testing page"