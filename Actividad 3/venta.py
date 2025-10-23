from dataclasses import dataclass, field
from typing import List, Dict
from decoradores import registrar_accion
from producto import Producto
from cliente import Cliente

@dataclass
class Venta:
    """
    Clase que representa una venta realizada por un cliente.
    Tiene composicion con producto
    """
    cliente = Cliente
    productos: List[Dict[str, any]] = field(default_factory=list)

    @registrar_accion("Se agrego un producto a una venta")
    def agregar_producto(self, producto: Producto, cantidad: int) ->None:
        """
        Agregar un producto a la venta si hay stock suficiente.
        """
