from config import *
from estiba import *
from lingada import *
from utils import *
import numpy as np
import random
from funcion_aptitud import *
from deap import base, creator, tools, algorithms

# ------------------------------------------
# BIBLIOTECAS UTILIZADAS:
# pip install deap numpy pandas openpyxl matplotlib 
## ------------------------------------------

## ------------------------------------------
# GENERAR EJECUTABLE EN LA CARPETA DIST:
# pyinstaller --onefile --icon=icono.png --add-data="datos_originales.xlsx;." algoritmo.py
# ------------------------------------------

# ------------------------------------------
# INICIALIZACIÓN DEL ALGORITMO
# ------------------------------------------

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

#CROMOSOMA: [ESTIBA_1, ESTIBA_2... ESTIBA_N] 
#Habrá tantos genes como cantidad de lingadas. 
#Habrá tantos genes distintos como estibas.


toolbox.register("gene", lambda: (random.randint(0, NUM_ESTIBAS - 1)))
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.gene, n=NUM_LINGADAS)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", evaluar_individuo)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", mutar_individuo, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# ------------------------------------------
# EJECUCIÓN DEL ALGORITMO
# ------------------------------------------

def ejecutar_algoritmo_genetico(generaciones=20, tam_pob=50):
    poblacion = toolbox.population(n=tam_pob)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values[0])
    stats.register("max", np.max)
    stats.register("avg", np.mean)

    poblacion, log = algorithms.eaSimple(poblacion, toolbox,
                                     cxpb=0.7, mutpb=0.2,
                                     ngen=generaciones,
                                     stats=stats, halloffame=hof,
                                     verbose=True)
    return hof[0], log

# ------------------------------------------
# MAIN
# ------------------------------------------

if __name__ == "__main__":
    mejor_solucion, log = ejecutar_algoritmo_genetico()
    print("\nMejor asignación:")
    resultado = reconstruir_niveles(mejor_solucion)
    for i, estiba_id, nivel in resultado:
        estiba_nombre = next(e.nombre for e in estibas if e.id == estiba_id)
        print(f"Lingada {i} → Estiba '{estiba_nombre}', Nivel {nivel}")

   
    graficar_lingadas_por_estiba(lingadas, resultado, estibas, nombre_archivo="grafico_lingadas.png")
    graficar_evolucion(log, nombre_archivo="evolucion_fitness.png")



