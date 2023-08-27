from fastapi import FastAPI
from petmanager import PetManager
from modules.datamodel import Animal
from typing import List


app = FastAPI()
app.mgr=PetManager()

@app.get("/api/v1/list")
async def list() -> List[Animal]:
    return app.mgr.list_animals()

@app.put('/api/v1/add')
async def create(animal: Animal) -> bool:
    return app.mgr.add_animal(animal)

@app.delete('/api/v1/delete/{id}')
async def delete(id: int) -> bool:
    return app.mgr.delete_animal(id)

@app.get('/api/v1/search/{id}')
async def get(id: int) -> bool:
    return app.mgr.get_animal(id)