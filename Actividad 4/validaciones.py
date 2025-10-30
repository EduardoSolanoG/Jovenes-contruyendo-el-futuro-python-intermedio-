import logging

# Configuración de depuracion
logging.basicConfig(level=logging.DEBUG, format='[DEBUG] %(message)s')



# FUNCIONES DE VALIDACION


def validar_nombre(nombre):
    """Valida que el nombre sea una cadena no vacía."""
    if not isinstance(nombre, str) or nombre.strip() == "":
        raise ValueError("El nombre debe ser una cadena de texto no vacía.")
    logging.debug(f"Nombre '{nombre}' validado correctamente.")


def validar_edad(edad):
    """Valida que la edad sea un número entero mayor que cero."""
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un número entero.")
    if edad <= 0:
        raise ValueError("La edad debe ser mayor que cero.")
    logging.debug(f"Edad '{edad}' validada correctamente.")


def validar_correo(correo):
    """Valida que el correo contenga '@' y termine con un dominio valido."""
    dominios_validos = (".com", ".mx", ".edu", ".org", ".net", ".gob", ".es", ".us")

    if not isinstance(correo, str):
        raise TypeError("El correo debe ser una cadena de texto.")

    if "@" not in correo:
        raise ValueError("El correo debe contener el simbolo '@'.")

    if not correo.endswith(dominios_validos):
        raise ValueError(f"El correo debe terminar en un dominio valido: {dominios_validos}")

    logging.debug(f"Correo '{correo}' validado correctamente.")



# FUNCIÓN PRINCIPAL DE PRUEBA


def validar_datos(nombre, edad, correo):
    """Coordina las validaciones y maneja los errores."""
    try:
        logging.debug("Iniciando validacion de datos...")
        validar_nombre(nombre)
        validar_edad(edad)
        validar_correo(correo)
        print(f"✅ Datos registrados correctamente: {nombre}, {edad} años, {correo}")

    except ValueError as ve:
        print(f"❌ Error de valor: {ve}")
    except TypeError as te:
        print(f"❌ Error de tipo: {te}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
    finally:
        print("➡ Finalizando proceso de validacion...\n")


def probar_validaciones():
    """Ejecuta diferentes pruebas con datos validos e invalidos."""
    print("=== Iniciando pruebas de validaciones ===")

    # Casos válidos
    validar_datos("Ana", 25, "ana@example.com")
    validar_datos("Luis", 30, "luis@unam.mx")

    # Casos inválidos
    validar_datos("", 20, "correo@example.com")  # Nombre vacío
    validar_datos("Pedro", -5, "pedro@example.com")  # Edad negativa
    validar_datos("Marta", 22, "martaexample.com")  # Falta arroba
    validar_datos("Carlos", 28, "carlos@example.xyz")  # Dominio no permitido
    validar_datos("Sofía", "veinte", "sofia@tec.edu")  # Edad tipo incorrecto

    # Ejemplo con error inesperado
    try:
        logging.debug("Probando division de edades...")
        resultado = 10 / 0  # Provoca ZeroDivisionError
    except ZeroDivisionError as zde:
        print(f"❌ Error de división: {zde}")

    print("=== Pruebas finalizadas ===")



# PROGRAMA PRINCIPAL

if __name__ == "__main__":
    probar_validaciones()
    print("\n🎉 ¡Felicidades! Has concluido con éxito el ejercicio de validación de datos.")