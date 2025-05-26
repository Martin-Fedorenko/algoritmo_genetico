from config import *
from carga_datos import *
from criterios_aptitud import *

# ------------------------------------------
# FUNCIÓN DE APTITUD
# ------------------------------------------
def evaluar_individuo(individuo):
    estiba_estado = {e.id: {"lingadas": []} for e in estibas}
    score = 0

    for idx, (estiba_id, lingada) in enumerate(zip(individuo, lingadas)):
        estiba = next(e for e in estibas if e.id == estiba_id)
        estado = estiba_estado[estiba_id]

        # Nivel automático: siguiente nivel disponible
        nivel = len(estado["lingadas"]) + 1

        # Penalización si supera el máximo de niveles
        if nivel > MAX_NIVELES_ESTIBA:
            score -= N5 * (nivel - MAX_NIVELES_ESTIBA)
            continue

        # Criterios de evaluación
        score += evaluar_agrupamiento(lingada, estado["lingadas"])
        score += evaluar_obstruccion(lingada, estado["lingadas"], nivel)
        score += evaluar_cercania_destino(lingada, estiba)
        score += evaluar_cercania_origen_destino(lingada, estiba)

        # Registrar la lingada con su nivel asignado
        estado["lingadas"].append({"lingada": lingada, "nivel": nivel})

    return (score,)

# Volvé a ejecutar la función de aptitud para obtener los niveles
def reconstruir_niveles(individuo):
    estiba_estado = {e.id: {"lingadas": []} for e in estibas}
    resultado = []

    for idx, (estiba_id, lingada) in enumerate(zip(individuo, lingadas)):
        estado = estiba_estado[estiba_id]
        nivel = len(estado["lingadas"]) + 1
        estado["lingadas"].append({"lingada": lingada, "nivel": nivel})
        resultado.append((idx, estiba_id, nivel))
    return resultado

