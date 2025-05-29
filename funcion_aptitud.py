from config import *
from carga_datos import *
from criterios_aptitud import *

# ------------------------------------------
# FUNCIÓN DE APTITUD
# ------------------------------------------

def evaluar_individuo(individuo):
    estiba_estado = {
    e.id: {"lingadas": [{"lingada": l} for l in e.lingadas]} for e in estibas}

    score = 0

    for (estiba_id, lingada) in zip(individuo, lingadas):
        estiba = next(e for e in estibas if e.id == estiba_id)
        estado = estiba_estado[estiba_id]

        # Nivel automático: siguiente nivel disponible
        nivel = len(estado["lingadas"]) + 1

        # Criterios de evaluación
        score += evaluar_agrupamiento(lingada, estado["lingadas"])
        score += evaluar_obstruccion(lingada, estado["lingadas"], nivel)
        score += evaluar_cercania_origen_destino(lingada, estiba)
        score += evaluar_cercania_zona(lingada, estiba)
        score -= evaluar_capacidad(nivel)

        # Registrar la lingada con su nivel asignado
        estado["lingadas"].append({"lingada": lingada})

    return (score,)
