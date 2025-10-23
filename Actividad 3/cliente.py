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
        """
        Simula el registro del cliente en el sistema
        En un caso real, podria guardarse en una base de datos o archivo JSON.
        """
        print(f"Cliente {self.nombre} registrado correctamente.")

    def agregar_comprar(self, compra: Dict) -> None:
        """
        Agrega una compra al historial del cliente.
        Esto aplica composicion indirecta: el cliente guarda ventas realizadas.
        """
        self.historial_compras.append(compra)

    def to_dict(self) -> Dict:
        """
        Extiende el metodovde Usuariopara incluir datos especificos del cliente.
        """
        data = super().to_dict()
        data.update({
            "telefono": self.telefono,
            "direccion": self.direccion,
            "historial_compras": self.historial_compras,
        })
        return data
