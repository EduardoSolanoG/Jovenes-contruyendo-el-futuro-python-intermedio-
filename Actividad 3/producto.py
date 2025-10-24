from dataclasses import dataclass, field
from decoradores import registrar_accion
from typing import Dict

@dataclass
class Producto:
    """
    Clase que representa un producto en la tienda.
    Responsable de manejar su informacion y stock.

    """
    nombre: str
    precio: float
    stock: int = field(default=0)

    def __post_init__(self):
        if self.precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        if self.stock < 0:
            raise ValueError("El stock no puede ser negativo.")

    def __str__(self):
        return (
            f"Producto: {self.nombre}\n"
            f"Precio_ ${self.precio:.2f}\n"
            f"Stock disponible: {self,stock} unidades"
        )

    @registrar_accion("Se actualizo el stock de un producto")
    def actualizar_stock(self, cantidad: int) -> None:
        """
        Modifica el stock. Puede ser positivo (entrada) o negativo (venta).
        """
        if self.stock + cantidad < 0:
            raise ValueError(f"No hay suficiente stock para retirar {abs(cantidad)} unidades.")
        self.stock += cantidad
        print(f"Stock actualizado. Nuevo stock de {self.nombre}: {self.stock}")

    @registrar_accion("Se modificó el precio de un producto")
    def actualizar_precio(self, nuevo_precio: float) -> None:
        """
        Actualiza el precio del producto, con validación.
        """
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor a 0.")
        anterior = self.precio
        self.precio = nuevo_precio
        print(f"Precio actualizado de {self.nombre}: ${anterior:.2f} → ${self.precio:.2f}")

    def to_dict(self) -> Dict:
        """
        Permite convertir un producto a formato diccionario para almacenar en JSON.
        """
        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }