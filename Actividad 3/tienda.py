from dataclasses import dataclass, field
from typing import List, Dict
from decoradores import registrar_accion
from producto import Producto
from venta import Venta
from cliente import Cliente

@dataclass
class Tienda:
    """
    Clase Tienda que administra inventario y ventas.
    Aplica Agregación: la tienda contiene ventas, pero estas existen independientemente.
    """
    nombre: str
    inventario: Dict[str, Producto] = field(default_factory=dict)   # Ej: {"Consola": Producto(...)}
    ventas_realizadas: List[Venta] = field(default_factory=list)

    @registrar_accion("Producto agregado al inventario")
    def agregar_producto(self, producto: Producto) -> None:
        """
        Agrega o actualiza un producto en el inventario de la tienda.
        """
        self.inventario[producto.nombre] = producto
        print(f"Producto '{producto.nombre}' disponible en tienda.")

    def mostrar_inventario(self) -> None:
        """
        Muestra todos los productos disponibles con su stock.
        """
        if not self.inventario:
            print("No hay productos en el inventario.")
            return

        print("\nInventario de la tienda:")
        for producto in self.inventario.values():
            print(f" - {producto.nombre}: ${producto.precio:.2f} | Stock: {producto.stock}")

    @registrar_accion("Se registró una venta en la tienda")
    def registrar_venta(self, venta: Venta) -> None:
        """
        Agrega una venta al historial de la tienda.
        """
        self.ventas_realizadas.append(venta)
        print(f"Venta registrada. Cliente: {venta.cliente.nombre}")

    def ventas_totales(self) -> float:
        """
        Retorna el total de dinero recaudado por todas las ventas.
        """
        return sum(venta.calcular_total() for venta in self.ventas_realizadas)

    def mostrar_ventas(self) -> None:
        """
        Muestra todas las ventas realizadas.
        """
        if not self.ventas_realizadas:
            print("No se han realizado ventas aún.")
            return

        print("\nVentas realizadas:")
        for venta in self.ventas_realizadas:
            print(venta)

    def productos_mas_vendidos(self) -> Dict[str, int]:
        """
        Retorna un diccionario con productos y cantidades vendidas.
        """
        conteo = {}
        for venta in self.ventas_realizadas:
            for item in venta.productos:
                nombre = item['producto'].nombre
                cantidad = item['cantidad']
                conteo[nombre] = conteo.get(nombre, 0) + cantidad
        return conteo