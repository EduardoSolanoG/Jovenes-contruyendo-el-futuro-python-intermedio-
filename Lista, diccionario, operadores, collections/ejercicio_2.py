from collections import Counter, OrderedDict

#datos
compras = {
    "luis", "Ana", "Luis",
    "carlos", "Martha", "Ana",
    "Sofia", "Elena", "Luis", "Carlos"
}

registro = {
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

