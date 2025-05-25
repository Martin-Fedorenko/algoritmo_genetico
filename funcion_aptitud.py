from config import *
from criterios_aptitud import *
import random
import numpy as np

# ------------------------------------------
# FUNCIÓN DE APTITUD
# ------------------------------------------

# Simulamos datos para lingadas y estibas
lingadas = [{
    "id": i,
    "orden": random.randint(1, 10),
    "colada": random.randint(1, 5),
    "producto": random.randint(1, 3),
    "fecha_salida": random.randint(1, 30),
    "centro_origen": random.randint(1, 5),
    "centro_destino": random.randint(1, 5),
    "volumen": random.uniform(0.5, 1.5)
} for i in range(NUM_LINGADAS)]

estibas = [{
    "id": j,
    "capacidad": 5.0,
    "ubicacion": random.randint(1, 5)
} for j in range(NUM_ESTIBAS)]


# ------------------------------------------
# FUNCIÓN DE APTITUD
# ------------------------------------------

def evaluar_individuo(individuo):
    estiba_estado = {e["id"]: {"volumen": 0, "lingadas": []} for e in estibas}
    score = 0

    for gen, lingada in zip(individuo, lingadas):
        estiba_id, nivel = gen
        estiba = next(e for e in estibas if e["id"] == estiba_id)
        estado = estiba_estado[estiba_id]

        # Agrupamiento
        for otra in estado["lingadas"]:
            if otra["orden"] == lingada["orden"]:
                score += N1
            if otra["colada"] == lingada["colada"]:
                score += N1
            if otra["producto"] == lingada["producto"]:
                score += N1

            # Obstrucción
            if otra["fecha_salida"] < lingada["fecha_salida"] and otra["nivel"] > nivel:
                score -= N2 * (otra["nivel"] - nivel)

        # Capacidad
        nuevo_volumen = estado["volumen"] + lingada["volumen"]
        if nuevo_volumen <= estiba["capacidad"]:
            # Eficiencia de carga
            if lingada["volumen"] > 1.2 and nuevo_volumen < estiba["capacidad"] * 0.5:
                score += N3
            if lingada["volumen"] < 0.8 and nuevo_volumen > estiba["capacidad"] * 0.8:
                score += N4
        else:
            score -= N5  # sobrecapacidad

        # Actualizar estiba
        estado["volumen"] = nuevo_volumen
        estado["lingadas"].append({**lingada, "nivel": nivel})

        # Cercanía centro siguiente
        distancia_destino = calcular_distancia(lingada["centro_destino"], estiba["ubicacion"])
        score += max(0, N6 - distancia_destino)

        # Cercanía origen/destino
        dist_origen = calcular_distancia(lingada["centro_origen"], estiba["ubicacion"])
        dist_destino = calcular_distancia(lingada["centro_destino"], estiba["ubicacion"])
        score += max(0, N7 - (dist_origen + dist_destino))

    return (score,)