from usuario import Usuario
from decoradores import registrar_accion
from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class Cliente(Usuario):
"""
Clase Cliente que hereda de Usuario.
Representa a un cliente del sistema de ventas.
"""
telefono: str = ""
direccion: str = ""
historial_compras: List[Dict] = field(default_factory=list)

@registar_accion("Se mostro la informacion de un cliente")
def mostrar_info(self) -> str:
    """
    Implementacion del metodo abstracto.
    Devuelve la informacion del cliente en un formato legible.
    """
    return (
        f"Nombre: {self.nombre}\n"
        f"Email: {self.email}\n"
        f"Telefono: {self.telefono}\n"
        f"Direccion: {self.direccion}\n"
        f"Historial de compras: {len(self.historial_compras)} ventas registradas\n"
    )

@registrar_accion("Cliente registrado en el sistema")
def registrar(self) -> None: