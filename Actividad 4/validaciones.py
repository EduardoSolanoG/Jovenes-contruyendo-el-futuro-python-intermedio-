import logging

# Configuración del modo depuración
logging.basicConfig(level=logging.DEBUG, format='[DEBUG] %(message)s')



# FUNCIONES DE VALIDACIÓN


def validar_nombre(nombre):
    """Valida que el nombre sea una cadena de texto no vacía y sin números."""
    if type(nombre) != str or nombre.strip() == "":
        raise ValueError(f"El nombre '{nombre}' no es válido. Debe ser texto y no estar vacío.")

    # Verificar que el nombre solo contenga letras y espacios
    if not all(c.isalpha() or c.isspace() for c in nombre):
        raise ValueError(f"El nombre '{nombre}' no es válido. No debe contener números ni símbolos.")

    logging.debug(f"Nombre '{nombre}' validado correctamente.")


def validar_edad(edad):
    """Valida que la edad sea un número entero mayor que cero."""
    if type(edad) != int:
        raise TypeError(f"La edad '{edad}' no es válida. Debe ser un número entero.")
    if edad <= 0:
        raise ValueError(f"La edad '{edad}' no es válida. Debe ser mayor que cero.")
    logging.debug(f"Edad '{edad}' validada correctamente.")


def validar_correo(correo):
    """Valida que el correo contenga '@' y termine en un dominio válido."""
    dominios_validos = (".com", ".mx", ".edu", ".org", ".net", ".gob", ".es", ".us")

    if type(correo) != str:
        raise TypeError(f"El correo '{correo}' no es una cadena de texto.")
    if "@" not in correo:
        raise ValueError(f"El correo '{correo}' no contiene el símbolo '@'.")
    if not correo.endswith(dominios_validos):
        raise ValueError(f"El correo '{correo}' no termina en un dominio válido. "
                         f"Dominios permitidos: {dominios_validos}")
    logging.debug(f"Correo '{correo}' validado correctamente.")


def validar_datos(nombre, edad, correo):
    """Coordina las validaciones y maneja los errores."""
    try:
        logging.debug("Iniciando validación de datos...")
        validar_nombre(nombre)
        validar_edad(edad)
        validar_correo(correo)
        print(f"Datos registrados correctamente: {nombre}, {edad} años, {correo}")

    except ValueError as e:
        print(f"Error de valor: {e}")
    except TypeError as e:
        print(f"Error de tipo: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        print("➡ Finalizando proceso de validación...\n")


def probar_validaciones():
    """Ejecuta diferentes pruebas con datos válidos e inválidos."""
    print("=== Iniciando pruebas de validaciones ===")

    # Casos válidos
    validar_datos("Ana", 25, "ana@example.com")
    validar_datos("Luis", 30, "luis@unam.mx")

    # Casos inválidos
    validar_datos("", 20, "correo@example.com")
    validar_datos("Pedro", -5, "pedro@example.com")
    validar_datos("Marta", "veinte", "martaexample.com")
    validar_datos("Carlos", 28, "carlos@example.xyz")
    validar_datos("Sofía", 22, "")

    # Ejemplo con error inesperado
    try:
        logging.debug("Probando división de edades...")
        resultado = 10 / 0  # Provoca ZeroDivisionError
    except ZeroDivisionError as zde:
        print(f"Error de división: {zde}")

    print("=== Pruebas finalizadas ===\n")


def registro_manual():
    """Permite ingresar los datos manualmente y validarlos."""
    print("=== Registro manual de usuario ===")
    try:
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        correo = input("Ingrese su correo: ")

        validar_datos(nombre, edad, correo)

    except ValueError as e:
        print(f"Error en los datos ingresados: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        print("Proceso de registro manual finalizado.\n")



# PROGRAMA PRINCIPAL


if __name__ == "__main__":
    probar_validaciones()
    registro_manual()
    print("¡Felicidades! Has concluido con éxito el ejercicio de validación de datos.")