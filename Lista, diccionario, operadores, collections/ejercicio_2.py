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
