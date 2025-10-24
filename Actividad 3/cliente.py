from usuario import Usuario
from decoradores import registrar_accion
from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class Cliente(Usuario):
    telefono: str = ""
    direccion: str = ""
    historial_compras: List[Dict] = field(default_factory=list)

    @registrar_accion("Se mostró la información de un cliente")
    def mostrar_info(self) -> str:
        return (
            f"--- Cliente ---\n"
            f"Nombre: {self.nombre}\n"
            f"Email: {self.email}\n"
            f"Teléfono: {self.telefono}\n"
            f"Dirección: {self.direccion}\n"
            f"Historial de compras: {len(self.historial_compras)} ventas registradas\n"
        )

    @registrar_accion("Cliente registrado en el sistema")
    def registrar(self) -> None:
        print(f"Cliente {self.nombre} registrado correctamente.")

    def agregar_compra(self, compra: Dict) -> None:
        self.historial_compras.append(compra)

    def to_dict(self) -> Dict:
        data = super().to_dict()
        data.update({
            "telefono": self.telefono,
            "direccion": self.direccion,
            "historial_compras": self.historial_compras
        })
        return data
