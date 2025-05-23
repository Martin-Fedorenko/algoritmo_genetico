import config
import random
import numpy as np
from deap import base, creator, tools



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


#Inicializacion de deap
# ------------------------------------------
# REPRESENTACIÓN: INDIVIDUO = lista de (estiba_id, nivel)
# ------------------------------------------

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

toolbox.register("gene", lambda: (random.randint(0, NUM_ESTIBAS - 1), random.randint(1, MAX_NIVELES)))
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.gene, n=NUM_LINGADAS)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", evaluar_individuo)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutUniformInt, low=[0, 1], up=[NUM_ESTIBAS - 1, MAX_NIVELES], indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# ------------------------------------------
# EJECUCIÓN DEL ALGORITMO
# ------------------------------------------

def ejecutar_algoritmo_genetico(generaciones=50, tam_pob=100):
    poblacion = toolbox.population(n=tam_pob)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values[0])
    stats.register("max", np.max)
    stats.register("avg", np.mean)

    poblacion, log = tools.eaSimple(poblacion, toolbox,
                                     cxpb=0.7, mutpb=0.2,
                                     ngen=generaciones,
                                     stats=stats, halloffame=hof,
                                     verbose=True)
    return hof[0], log

# ------------------------------------------
# EJECUTAR
# ------------------------------------------

if __name__ == "__main__":
    mejor_solucion, log = ejecutar_algoritmo_genetico()
    print("\nMejor asignación:")
    for i, (estiba_id, nivel) in enumerate(mejor_solucion):
        print(f"Lingada {i} → Estiba {estiba_id}, Nivel {nivel}")
