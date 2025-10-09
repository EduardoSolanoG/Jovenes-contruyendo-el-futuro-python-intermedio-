# Importamos las librerías necesarias
from functools import reduce   # para usar reduce()
import time

#generador de datos
def leer_temperaturas():
    datos = [
        ("CDMX", 26),
        ("Monterrey", 34),
        ("Toluca", 19),
        ("Cancún", 38),
        ("Guadalajara", 31),
        ("Puebla", 22),
    ]
    # Con 'yield' devolvemos cada tupla una por una
    for dato in datos:
        yield dato


#decorador personalizado
def auditar_funcion(func):
    # usamos un diccionario para conservar el conteo entre llamadas
    contador = {"llamadas": 0}

    def wrapper(*args, **kwargs):
        # Se ejecuta antes de la función decorada
        contador["llamadas"] += 1
        print(f"\n🧩 Ejecutando función: {func.__name__} (Llamada #{contador['llamadas']})")

        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()

        print(f"⏱️ Duración: {fin - inicio:.4f} segundos")
        return resultado

    return wrapper  # devolvemos la función modificada


#funciones de apoyo (en lugar de lambda)
def es_calor_extremo(registro):
    #Determina si la temperatura de un registro es mayor o igual a 30°C.
    ciudad, temperatura = registro
    return temperatura >= 30

def mensaje_alerta(registro):
    # Convierte una tupla (Ciudad, Temperatura) en un mensaje de texto.
    ciudad, temperatura = registro
    return f"Alerta de calor en {ciudad}: {temperatura}°C"

def obtener_temperatura(registro):
    #Devuelve solo la temperatura de un registro.
    ciudad, temperatura = registro
    return temperatura

def acumular_temperatura(acumulador, registro):
    #Suma la temperatura actual al acumulador total.
    ciudad, temperatura = registro
    return acumulador + temperatura


#funcion principal de procesamiento
@auditar_funcion
def procesar_temperaturas():
    #Función principal que procesa los datos del generador.
    #Aplica filtrado, ordenamiento, transformación y cálculo de promedio
    #usando funciones normales (sin lambda).

    # Obtener datos desde el generador
    datos = list(leer_temperaturas())

    # Filtrar temperaturas mayores o iguales a 30°C
    altas = list(filter(es_calor_extremo, datos))

    #  Ordenar las temperaturas de mayor a menor
    ordenadas = sorted(altas, key=obtener_temperatura, reverse=True)

    #  Transformar cada registro en un mensaje de alerta
    alertas = list(map(mensaje_alerta, ordenadas))

    #  Calcular el promedio de las temperaturas altas
    if altas:  # evitamos división por cero
        suma = reduce(acumular_temperatura, altas, 0)
        promedio = suma / len(altas)
    else:
        promedio = 0

    #  Mostrar resultados finales
    print("\n🔥 Alertas ordenadas:")
    for alerta in alertas:
        print("  -", alerta)

    print(f"\n🌡️ Temperatura promedio de alertas: {promedio:.1f}°C")


def main():
    #Función principal del programa.
    print("=== Sistema de Monitoreo Ambiental Inteligente ===")
    procesar_temperaturas()
    print("\n✅ Ejecución completada.")


if __name__ == "__main__":
    main()