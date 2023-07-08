from fastapi import FastAPI

from modules.datamodel import Animal


app = FastAPI()
app.mgr=PetManager()

@app.get("/api/v1/list")
async def list():
    return app.mgr.list()

@app.create('/api/v1/add')
async def create(animal: Animal):
    return app.mgr.add_animal(animal)

    #TESTTESTTEST

#To run:
#pip install uvicorn
#uvicorn server-fastapi:app

# http://localhost:8000/docs 
# https://fastapi.tiangolo.com/