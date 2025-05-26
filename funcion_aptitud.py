from config import *
from lingadas import *
from estibas import *
from criterios_aptitud import *

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

        score += evaluar_agrupamiento(lingada, estado["lingadas"])
        score += evaluar_obstruccion(lingada, estado["lingadas"], nivel)
        score += evaluar_capacidad_y_carga(lingada, estado["volumen"], estiba["capacidad"])
        score += evaluar_cercania_destino(lingada, estiba)
        score += evaluar_cercania_origen_destino(lingada, estiba)

        # Actualizar estado de la estiba
        estado["volumen"] += lingada["volumen"]
        estado["lingadas"].append({**lingada, "nivel": nivel})

    return (score,)
