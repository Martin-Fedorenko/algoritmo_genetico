from config import *
import numpy as np
from carga_datos import CENTROS

# ------------------------------------------
# CRITERIOS DE APTITUD
# ------------------------------------------

def evaluar_obstruccion(lingada, otras_lingadas, nivel_actual):
    score = 0
    for otra_entry in otras_lingadas:
        otra = otra_entry["lingada"]
        nivel_otra = otra_entry["nivel"]

        if otra.finish_date_prg and lingada.finish_date_prg:
            if otra.finish_date_prg < lingada.finish_date_prg and nivel_otra > nivel_actual:
                score -= N2 * (nivel_otra - nivel_actual)
    return score

def evaluar_agrupamiento(lingada, otras_lingadas):
    score = 0
    for otra_entry in otras_lingadas:
        otra = otra_entry["lingada"]  # accedemos al objeto Lingada dentro del dict
        if otra.orden == lingada.orden:
            score += N1
        if otra.colada == lingada.colada:
            score += N1
        if otra.producto == lingada.producto:
            score += N1
    return score

def calcular_distancia(a, b):
    def get_coords(valor):
        if isinstance(valor, str) and valor in CENTROS:
            return CENTROS[valor]
        elif isinstance(valor, (tuple, list)) and len(valor) == 2:
            return tuple(valor)
        else:
            raise ValueError(f"Ubicación inválida: {valor}")

    a_coord = get_coords(a)
    b_coord = get_coords(b)
    
    return ((a_coord[0] - b_coord[0])**2 + (a_coord[1] - b_coord[1])**2)**0.5

def evaluar_cercania_destino(lingada, estiba):
    distancia = calcular_distancia(lingada.centro_destino, estiba.ubicacion)
    return max(0, N6 - distancia)

def evaluar_cercania_origen_destino(lingada, estiba):
    dist_origen = calcular_distancia(lingada.centro_origen, estiba.ubicacion)
    dist_destino = calcular_distancia(lingada.centro_destino, estiba.ubicacion)
    return max(0, N7 - (dist_origen + dist_destino))
