from config import *
from carga_datos import *
import matplotlib.pyplot as plt
import random


def mutar_individuo(individuo, indpb):
    for i in range(len(individuo)):
        if random.random() < indpb:
            individuo[i] = random.randint(0, NUM_ESTIBAS - 1)
    return individuo,

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

def reconstruir_niveles(individuo):
    # Inicializar estado de estibas con lingadas cargadas (sin usar .nivel)
    estiba_estado = {
        e.id: {
            "lingadas": [{"lingada": l} for l in e.lingadas]  # No consideramos el nivel original
        }
        for e in estibas
    }

    resultado = []

    for idx, (estiba_id, lingada) in enumerate(zip(individuo, lingadas)):
        estado = estiba_estado[estiba_id]

        # Nivel es el siguiente número disponible (cantidad de lingadas ya acumuladas + 1)
        nivel = len(estado["lingadas"]) + 1

        # Agregamos la nueva lingada al estado de la estiba
        estado["lingadas"].append({"lingada": lingada})

        # Registramos el resultado con su nivel calculado
        resultado.append((idx, estiba_id, nivel))

    return resultado

def graficar_evolucion(log):
    gen = log.select("gen") if hasattr(log, "select") else list(range(len(log)))
    max_fitness = log.select("max")

    plt.figure(figsize=(10, 5))
    plt.plot(gen, max_fitness, marker="o", linestyle="-", color="blue", label="Fitness Máximo")
    plt.title("Evolución del Fitness Máximo por Generación")
    plt.xlabel("Generación")
    plt.ylabel("Fitness")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

