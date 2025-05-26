from config import *
from criterios_aptitud import *

import numpy as np

# ------------------------------------------
# CRITERIOS DE APTITUD
# ------------------------------------------

def evaluar_agrupamiento(lingada, otras_lingadas):
    score = 0
    for otra in otras_lingadas:
        if otra["orden"] == lingada["orden"]:
            score += N1
        if otra["colada"] == lingada["colada"]:
            score += N1
        if otra["producto"] == lingada["producto"]:
            score += N1
    return score

def evaluar_obstruccion(lingada, otras_lingadas, nivel_actual):
    score = 0
    for otra in otras_lingadas:
        if otra["fecha_salida"] < lingada["fecha_salida"] and otra["nivel"] > nivel_actual:
            score -= N2 * (otra["nivel"] - nivel_actual)
    return score

def evaluar_capacidad_y_carga(lingada, volumen_actual, capacidad):
    nuevo_volumen = volumen_actual + lingada["volumen"]
    score = 0
    if nuevo_volumen <= capacidad:
        if lingada["volumen"] > 1.2 and nuevo_volumen < capacidad * 0.5:
            score += N3
        if lingada["volumen"] < 0.8 and nuevo_volumen > capacidad * 0.8:
            score += N4
    else:
        score -= N5  # penalización por sobrecapacidad
    return score

def calcular_distancia(a, b):
    return abs(a - b)

def evaluar_cercania_destino(lingada, estiba):
    distancia = calcular_distancia(lingada["centro_destino"], estiba["ubicacion"])
    return max(0, N6 - distancia)

def evaluar_cercania_origen_destino(lingada, estiba):
    dist_origen = calcular_distancia(lingada["centro_origen"], estiba["ubicacion"])
    dist_destino = calcular_distancia(lingada["centro_destino"], estiba["ubicacion"])
    return max(0, N7 - (dist_origen + dist_destino))


