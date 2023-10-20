import os
import logging
import requests
logging.basicConfig(level=os.environ.get('LOGLEVEL', 'INFO'))


logger=logging.getLogger(__name__)

from petmanager.datamodel import Animal
from typing import List, Tuple

SERVER=os.getenv('SERVER','http://localhost:8000')

class PetManagerClient:
    def __init__(self, server) -> None:
        logger.debug(f"petmanager init, server={server}")
        self.server=server

    def add_animal(self, animal: Animal) -> bool:
        r=requests.post(self.server+'/add', json=animal)
        return r.json()

    def list_animals(self, species: str = None, gender: bool = None) -> List[Animal]:
        r=requests.get(self.server+'/list')
        return r.json()

    def del_animal(self, id: int = None) -> bool:
        r=requests.delete(self.server+f'/del/{id}')
        return r.json()
    
    def get_animal(self, id: int = None) -> Animal:
        r=requests.post(self.server+f'/get')
        return r.json()


class Commands:
    add = 1
    search = 2
    list = 3
    delete = 4
    exit = 5


def main():
    print("Starting Pet Manager")
    mgr = PetManagerClient(SERVER)

    w = """Welcome to Pet manager! Please, choose command:
    1 - add animal;
    2 - search for an animal;
    3 - list all animals;
    4 - delete an animal;
    5 - exit
    Enjoy!"""

    print(w)

    while True:
        c = input("Enter command: ")
        try:
            command = int(c)
        except ValueError:
            print("Invalid command")
            command = 0
        if command == Commands.add:
            id = int(input("ID: "))
            name = input("NAME: ")
            g = input("Gender (M/F): ")
            gender_male = g == "M"
            species = input("Species: ")
            animal = Animal(id, gender_male, name, species)
            result = mgr.add_animal(animal)
            if result.success:
                print("OK")
            else:
                print(f"Error: {result.message}")

        if command == Commands.list:

            '''g=input("Gender (M/F, empty for all)")    
            print(f"DEBUG: gm={gm}")
            sp=input("Species (empty for all): ")
            sp=sp if sp != "" else None
            print(f"DEBUG: sp={sp}")'''
        
        
        al=mgr.list_animals(gender=gm, species=sp)
        print(al)
        if command == Commands.exit:
            print("Goodbye!")
            quit()
    # Other commands here
        if command == Commands.delete:
            print ("Input ID:")
            id_to_delete=int(input())
            de=mgr.delete_animal(id_to_delete)
            print(de)

        if command == Commands.search:
            id_to_search=int(input("Inpui ID: "))
            name_to_search=str(input("Input Name: "))
            se=mgr.get_animal(id_to_search, name_to_search)
            print(se)

if __name__=="__main__":
    main()