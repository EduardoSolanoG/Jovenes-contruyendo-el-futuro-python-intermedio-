from abc import ABC, abstractmethod
from typing import Dict
from dataclasses import dataclass, field

@dataclass
class Usuario(ABC):
    """
    Clase abstracta que actua como ´interfaz´para usuarios del sistema.
    Contiene atributos y metodos que deben implementar las subclases.
    Usamos dataclass para manejo sencillo de atributos.
    """
    nombre: str
    email: str
    _id: int = field(default=0, repr=False)

