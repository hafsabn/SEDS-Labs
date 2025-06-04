from fastapi import FastAPI
# Instantiating a FastAPI object handling all API routes
app = FastAPI()
# Creating a GET endpoint at the root path
@app.get("/")
async def hello_world():
    return {"hello": "world"}
# Async method returning a JSON response autmatically handled by FastAPI