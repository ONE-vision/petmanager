from dataclasses import dataclass


@dataclass
class Animal:
    id: int
    gender_male: bool
    name: str
    species: str = "dog"


@dataclass
class Result:
    success: bool = True
    message: str = None
