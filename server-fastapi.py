from fastapi import FastAPI
from petmanager import PetManager
from modules.datamodel import Animal


app = FastAPI()
app.mgr=PetManager()

@app.get("/api/v1/list")
async def list():
    return app.mgr.list_animals()

@app.put('/api/v1/add')
async def create(animal: Animal):
    return app.mgr.add_animal(animal)

@app.delete('/api/v1/delete')
async def delete(id, name):
    return app.mgr.delete_animal(bool)

    #TESTTESTTEST

#To run:
#pip install uvicorn
#uvicorn server-fastapi:app

# http://localhost:8000/docs 
# https://fastapi.tiangolo.com/