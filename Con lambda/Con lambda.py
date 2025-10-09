from functools import reduce
import time


#generador de datos
def leer_temperaturas():

    #Generador que devuelve una a una las tuplas (Ciudad, Temperatura).
    datos = [
        ("CDMX", 26),
        ("Monterrey", 34),
        ("Toluca", 19),
        ("Cancún", 38),
        ("Guadalajara", 31),
        ("Puebla", 22),
    ]
    # 'yield' devuelve uno por uno los valores
    for dato in datos:
        yield dato


#decorador personalizado
def auditar_funcion(func):

    #Decorador que imprime el nombre de la función ejecutada, cuenta cuántas veces se ha llamado y mide el tiempo de ejecución.
    contador = {"llamadas": 0}

    def wrapper(*args, **kwargs):
        contador["llamadas"] += 1
        print(f"\n🧩 Ejecutando función: {func.__name__} (Llamada #{contador['llamadas']})")
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"⏱️ Duración: {fin - inicio:.4f} segundos")
        return resultado

    return wrapper


#funcion principal de procesamiento
@auditar_funcion
def procesar_temperaturas():

    #Procesa las temperaturas usando funciones lambda, map, filter, sorted y reduce.

    # Obtener datos desde el generador
    datos = list(leer_temperaturas())

    # 🔹 Filtrar temperaturas mayores o iguales a 30°C
    altas = list(filter(lambda x: x[1] >= 30, datos))

    # 🔹 Ordenar por temperatura descendente
    ordenadas = sorted(altas, key=lambda x: x[1], reverse=True)

    # 🔹 Transformar cada tupla en un mensaje de alerta
    alertas = list(map(lambda x: f"Alerta de calor en {x[0]}: {x[1]}°C", ordenadas))

    # 🔹 Calcular el promedio de las temperaturas altas
    if altas:
        suma = reduce(lambda acc, x: acc + x[1], altas, 0)
        promedio = suma / len(altas)
    else:
        promedio = 0

    # 🔹 Mostrar resultados
    print("\n🔥 Alertas ordenadas:")
    for alerta in alertas:
        print("  -", alerta)

    print(f"\n🌡️ Temperatura promedio de alertas: {promedio:.1f}°C")


#funcion principal del programa
def main():

    #Punto de entrada principal del sistema.
    print("=== Sistema de Monitoreo Ambiental Inteligente ===")
    procesar_temperaturas()
    print("\n✅ Ejecución completada.")


if __name__ == "__main__":
    main()