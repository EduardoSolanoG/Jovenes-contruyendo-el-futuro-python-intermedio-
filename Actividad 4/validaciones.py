import logging
from logging import DEBUG

#configuracion del  modo depuracion
logging.basicConfig(level=logging.DEBUG, format="[DEBUG] %(message)s")

#Funciones de validacion

def validar_nombre(nombre):
    """Valida que el nombre sea una cadena no vacioa."""
    if not isinstance(nombre, str) or nombre.strip() == "":
        raise ValueError("El nombre debe ser una cadena de texto no vacia.")
    logging.debug(f"Nombre ´{nombre}´ validado correctamente.")


def validar_edad(edad):
    """Valida que la edad sea un numero entero mayor que cero."""
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un numero entero.")
    if edad <= 0:
        raise ValueError("La edad debe ser mayor que cero")
    logging.debug(f"Edad ´{edad}´ validada correctamente.")


def validar_correo(correo):
    """Valida que el correo contenga @ y un dominio valido (.com, .mx, .edu, etc)."""
    dominios_validos = (".com", ".mx", ".edu", ".org", ".net", ".gob", ".es", ".us")

    if not isinstance(correo, str):
        raise TypeError("El correo debe ser una cadena de texto.")

    if "@" not in correo:
        raise ValueError("El correo debe contener el simbolo ´@´.")

    if not correo.endswith(dominios_validos):
        raise ValueError(f"El correo debe terminar en un dominio valido: {dominios_validos}")

    logging.debug(f"Correo ´{correo}´ valido correctamente.")



#Funcion principal de prueba

def validar_datos(nombre, edad, correo):
    """Coordina las validaciones y maneja los errores."""
    try:
        logging.debug("Iniciando validacion de datos...")
        validar_nombre(edad)
        validar_edad(edad)
        validar_correo(correo)
        print(f"Datos registrados correctamente: {nombre}, {edad} años,{correo}")


