from collections import Counter, OrderedDict

#datos
compras = {
    "compras": ["luis", "Ana",
    "Luis", "carlos", "Martha", "Ana",
    "Sofia", "Elena", "Luis", "Carlos",]
}

registros = {
    "registrados": ["Ana", "Carlos", "Martha", "Elena"]
}

#filtrar clientes nuevos
def filtrar_clientes_nuevos(dic_compras, dic_registrados):
    diferencia = lambda c, r: list(set(c) - set(r))
    return {"clientes_nuevos": diferencia(dic_compras["compras"],dic_registrados["registros"])}

#Eliminar dupicados conservando el orden
def eliminar_duplicados(dic_compras):
    sin_duplicados = list(OrderedDict.fromkeys(dic_compras["compras"]))
    return {"clientes_unicos": sin_duplicados}


#contar cuantas veces compra el cliente
def contar_compras(dic_compras):
    contador = Counter(dic_compras["compras"])
    return {"frecuencia_compras": dict(contador)}

#crear un resumen para clientes frecuentes
def crear_resumen(dic_frecuencias):
    resumen = {
        cliente: f"H comprado{veces} veces"
        for cliente, veces in dic_frecuencias["frecuencia_compras"].items()
        if veces >1
    }
    return {"resumen_clientes": resumen}

#funcion principal que une todo
def sistema_clientes(dic_compras, dic_registrados):
    nuevos = filtrar_clientes_nuevos(dic_compras, dic_registrados)
    unicos = eliminar_duplicados(dic_compras)
    frecuencia = contar_compras(dic_compras)
    resumen = crear_resumen(frecuencia)
    return {
        "clientes_nuevos": nuevos["clientes_nuevo"],
        "clientes_unicos": unicos["clientes_unicos"],
        "resumen_clientes": resumen["resumen_clientes"]
    }

#============================
#Ejecucion directa
#============================

resultado = sistema_clientes(compras, registros)
print("Clientes nuevos no registrados:")
print(resultado["clientes_nuevos"])

print("\n Lista de clientes unicos:")
print(resultado["clientes_unicos"])

print("\n Resumen por clientes frecuentes:")
for cliente, mensaje in resultado["resumen_clientes"].items():
    print(f"{cliente}: {mensaje}")


if __name__ == "__main__":
    pass