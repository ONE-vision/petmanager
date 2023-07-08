from fastapi import FastAPI
from petmanager import PetManager
from modules.datamodel import Animal


app = FastAPI()
app.mgr=PetManager()

@app.get("/api/v1/list_animals")
async def list():
    return app.mgr.list_animals()

@app.put('/api/v1/add')
async def create(animal: Animal):
    return app.mgr.add_animal(animal)

# To run:
#pip install uvicorn
#uvicorn server-fastapi:app

# http://localhost:8000/docs 
# https://fastapi.tiangolo.com/
