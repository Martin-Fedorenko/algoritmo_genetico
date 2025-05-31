from config import *
from utils import *

# ------------------------------------------
# CRITERIOS DE APTITUD
# ------------------------------------------

def evaluar_agrupamiento(lingada, otras_lingadas):
    score = 0
    for otra_entry in otras_lingadas:
        otra = otra_entry["lingada"]
        if otra.orden == lingada.orden:
            score += N1
        if otra.colada == lingada.colada:
            score += N1
        if otra.producto == lingada.producto:
            score += N1
    return score

def evaluar_obstruccion(lingada, otras_lingadas, nivel_actual):
    if not lingada.finish_date_prg:
        return 0

    penalizacion_total = 0

    for nivel_inferior, otra_entry in enumerate(otras_lingadas, start=1):
        otra = otra_entry["lingada"]

        if otra.finish_date_prg and otra.finish_date_prg < lingada.finish_date_prg:
            penalizacion = (nivel_actual - nivel_inferior + 1) * N2
            penalizacion_total -= penalizacion

    return penalizacion_total

def evaluar_cercania_zona(lingada, estiba):

    x_centro, y_centro = CENTROS[lingada.centro_destino]
    mitad_lado = LADO_ZONA_CENTRO / 2
    x_min = x_centro - mitad_lado
    x_max = x_centro + mitad_lado
    y_min = y_centro - mitad_lado
    y_max = y_centro + mitad_lado

    x_estiba, y_estiba = estiba.ubicacion

    if x_min <= x_estiba <= x_max and y_min <= y_estiba <= y_max:
        return N3
    return 0

def evaluar_cercania_origen_destino(lingada, estiba):
    dist_origen = calcular_distancia(lingada.centro_origen, estiba.ubicacion)
    dist_destino = calcular_distancia(lingada.centro_destino, estiba.ubicacion)
    return max(0, N4 - (dist_origen + dist_destino))

def evaluar_capacidad(nivel):
    # Nivel 1 es menos ocupado, niveles más altos indican mayor ocupación
    # Cuanto menor el nivel, mayor el puntaje (por ejemplo N6 es la constante para este criterio)
    if nivel <= MAX_NIVELES_ESTIBA:
        return N6 * (MAX_NIVELES_ESTIBA - nivel + 1)
    else:
        # Penalizar si supera niveles permitidos (opcional)
        return -N5 * (nivel - MAX_NIVELES_ESTIBA)

    
