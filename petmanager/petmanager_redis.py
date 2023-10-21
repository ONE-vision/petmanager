import logging
logging.basicConfig(level=logging.INFO)
import os
import redis

logger=logging.getLogger(__name__)

from .datamodel import Animal, Result
from typing import List, Tuple
REDIS_HOST=os.environ.get('REDIS_HOST')
REDIS_PORT=int(os.environ.get('REDIS_PORT', 6379))


class PetManager_Redis:
    def __init__(self) -> None:
        logger.debug("PetManager_Redis init")
        self.r=redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

    def _validate(self, animal: Animal) -> bool:
        logger.debug("in validate")
        """check if we can accept this animal.
        Checks:
            1. species is "dog" or "cat"
            2. id is unique
        """
        if self.r.get(animal.id):
            logger.warning(f"Duplicate id {id}")
            return False
        if animal.species not in ['cat', 'dog']:
            logger.warning(f"Bad species {animal.species}!")
            return False
        logger.info(f"Animal accepted: {animal}")
        return True

    def add_animal(self, animal: Animal) -> bool:
        if  self._validate(animal):
            self.r.set(animal.id, animal)
            return True
        return False

    def list_animals(self, species: str = None, gender: bool = None) -> List[Animal]:
        """
        return list of animal objects, if "species"or "gender" are specified - return only
        animals with specified parameters. If none found = return an empty array.
        """
        result=[]
        for k in self.r.keys():
            a=self.r.get(k)
            if not (a.species==species or species==None):
                continue
            if not (a.gender==gender or gender == None):
                continue
            result.append(a)
        return result

    def get_animal(self, id: int = None, name: str = None) -> Animal:
        """
        Return requested animal and search result.

        If id is passed - return the animal with given id
        if id and name are passed - return the animal with given id and given name, if exists
        if only name is given - return the only animal with this name. If more then 1 animals
        have this name - fail.
        The method should return object of type Animal if search was successful or None.
        """
        logger.debug(f"Get animal, id={id}, name={name}")
        if id != None:
            r=self.r.get(id)
            if not r:
               return None
            if name and r.name!=name:
                return None
            return r
        
        # we have no id (but probably name)
        if not name:
            raise RuntimeError("get_animal should have id or name")
        for i in self.r.keys():
            a=self.r.get(i)
            if a.name == name: 
                return a

                # return result

    def delete_animal(self, deleted: int) -> bool:
        """
        Delete from the list the animal with given id, if found.
        Return Result object with success=True if the animal deleted, else with success=False
        """
        return self.r.delete(deleted)

