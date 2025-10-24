from tienda import Tienda
from administrador import Administrador
from cliente import Cliente
from producto import Producto
from venta import Venta

def main():
    # 1. Crear tienda
    tienda = Tienda(nombre="TechStore")

    # 2. Crear administrador y autenticar
    admin = Administrador(nombre="Carlos", email="admin@techstore.com")
    if admin.autenticar("ADMIN123"):
        print("🔐 Administrador autenticado correctamente.\n")

    # 3. Crear productos y agregarlos al inventario
    productos = [
        Producto("Consola de videojuego", 11000, 10),
        Producto("Videojuego", 1500, 25),
        Producto("Control", 1800, 15),
        Producto("Audífonos gamer", 1100, 20),
        Producto("Memoria externa", 1150, 30)
    ]

    for p in productos:
        tienda.agregar_producto(p)

    tienda.mostrar_inventario()

    # 4. Crear un cliente
    cliente1 = Cliente(nombre="Eduardo", email="eduardo@mail.com", telefono="5551234567", direccion="CDMX, México")
    cliente1.registrar()

    # 5. Iniciar una venta
    venta1 = Venta(cliente=cliente1)

    # Agregar productos a la venta
    venta1.agregar_producto(tienda.inventario["Consola de videojuego"], 1)
    venta1.agregar_producto(tienda.inventario["Videojuego"], 2)

    # 6. Finalizar venta
    venta1.finalizar_venta()

    # 7. Registrar venta en tienda
    tienda.registrar_venta(venta1)

    # 8. Mostrar información
    print("\n=== INFORMACIÓN FINAL ===")
    print(f"Total recaudado por la tienda: ${tienda.ventas_totales():.2f}")

    print("\n📈 Productos más vendidos:")
    for nombre, cantidad in tienda.productos_mas_vendidos().items():
        print(f" - {nombre}: {cantidad} unidades")

    print("\n🧾 Historial de compras del cliente:")
    for compra in cliente1.historial_compras:
        print(compra)

    print("\n🏁 Fin del programa")

if __name__ == "__main__":
    main()