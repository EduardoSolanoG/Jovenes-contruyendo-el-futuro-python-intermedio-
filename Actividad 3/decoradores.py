from functools  import wraps
import datetime
from typing import Callable, Any

def registrar_accion(mensaje: str) ->callable:
    """
    decorador que registra una accion en consola con timestamp.
    Uso: @registrar_accion("descripcion de la accion
    """
    def decorador(func: callable) -> callable:
        def wrapper(*args, **kwargs) -> Any:
            resultado = func(*args, **kwargs)
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # registro simple en consola; en un sistema real podria ir a archivo o logger
            print(f"[{now}] {mensaje} - funcion: {func.__name__}")
            return resultado

        return wrapper

    return decorador