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

    def __post_init__(self):
        #Validaciones simples al crear un usuario
        if not isinstance(self.nombre, str) or not self.nombre.strip():
            raise ValueError("El nombre debe ser una cadena vacia.")
        if "@" not in self.email or "." not in self.email:
            raise ValueError("Email invalido.")

    @abstractmethod
    def mostrar_info(self) -> str:
        """
        Debe devolver una representacion textual del usuario.
        Cada subclase implementara su propio formato.
        """
        raise NotImplementedError

    def to_dict(self) -> Dict[str, str]:
        """
        Metodo comun para serializar atributos esenciales (util para guardarlo en JSON).
        No rompe la abstraccion: devuelve solo los datos basicos.
        """
        return {"id": self.id, "nombre": self.nombre, "email": self.email}

    #Metodo opcional que pueden reutilizar subclase (login simplificado)
    def auntentificar(self, token: str) -> bool:
        """
        Metodo base de autentificacion simplificada. En produccion, se usaria hashing/DB.
        Por defecto devuvelve True si token no vacio; las subclases pueden sobreescribir.
        """
        return bool(token and token.strip())
