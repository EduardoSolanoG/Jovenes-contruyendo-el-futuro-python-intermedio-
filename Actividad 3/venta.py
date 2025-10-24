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
    cliente: Cliente
    productos: List[Dict[str, any]] = field(default_factory=list)

    @registrar_accion("Se agrego un producto a una venta")
    def agregar_producto(self, producto: Producto, cantidad: int) ->None:
        """
        Agregar un producto a la venta si hay stock suficiente.
        """
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0.")

        if producto.stock < cantidad:
            raise ValueError(f"No hay stock suficiente para {producto.nombre}. Stock actual: {producto.stock}")

            # Disminuir stock del producto (composición directa)
        producto.actualizar_stock(-cantidad)

        # Agregar producto a la lista de la venta
        self.productos.append({"producto": producto, "cantidad": cantidad})
        print(f"✔ Producto '{producto.nombre}' agregado: {cantidad} unidades.")

    def calcular_total(self) -> float:
        """Calcula el total de la venta."""
        return sum(item["producto"].precio * item["cantidad"] for item in self.productos)

    @registrar_accion("Se registró una venta")
    def finalizar_venta(self) -> None:
        """Registra la venta al historial del cliente."""
        total = self.calcular_total()
        self.cliente.agregar_compra({
            "total": total,
            "productos": [(item["producto"].nombre, item["cantidad"]) for item in self.productos]
        })
        print(f"Venta finalizada. Total: ${total:.2f}")

    def __str__(self) -> str:
        productos_str = "\n".join(
            f" - {item['producto'].nombre} x {item['cantidad']} = ${item['producto'].precio * item['cantidad']:.2f}"
            for item in self.productos
        )
        return (
            f"--- Venta ---\nCliente: {self.cliente.nombre}\n"
            f"Productos:\n{productos_str}\n"
            f"Total: ${self.calcular_total():.2f}\n"
        )