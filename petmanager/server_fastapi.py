import logging
import uvicorn
from fastapi import FastAPI
from .petmanager import PetManager
from .datamodel import Animal
from typing import List
import os

LOGLEVEL=os.environ.get('LOGLEVEL','DEBUG')
logging.basicConfig(level=LOGLEVEL)
logger=logging.getLogger(__name__)

app = FastAPI()
if os.environ.get('REDIS_HOST', None):
    l.info("Using Redis")
    from .petmanager_redis import PetManager_Redis
    app.mgr=PetManager_Redis()
else:
    logger.info("REDIS_HOST not set, using in-memory Petmanager")
    from .petmanager import PetManager
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
async def get(id: int) -> Animal:
    return app.mgr.get_animal(id)

def main():
    uvicorn.run(app=app, port=int(os.getenv('HTTP_PORT', 8000 )), host="0.0.0.0")

if __name__ == "__main__":
    main()