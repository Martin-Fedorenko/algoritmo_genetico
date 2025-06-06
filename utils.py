from config import *
from carga_datos import *
import matplotlib.pyplot as plt
import random
from collections import Counter
import os
import sys
import subprocess


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
    estiba_estado = {
        e.id: {
            "lingadas": [{"lingada": l} for l in e.lingadas] 
        }
        for e in estibas
    }

    resultado = []

    for idx, (estiba_id, lingada) in enumerate(zip(individuo, lingadas)):
        estado = estiba_estado[estiba_id]

        nivel = len(estado["lingadas"]) + 1

        estado["lingadas"].append({"lingada": lingada})

        resultado.append((idx, estiba_id, nivel))

    return resultado

def graficar_evolucion(log, nombre_archivo="evolucion_fitness.png"):

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

    plt.savefig(nombre_archivo)

    try:
        os.startfile(nombre_archivo)
    except AttributeError:
        subprocess.run(["open" if sys.platform == "darwin" else "xdg-open", nombre_archivo])

    plt.close()


def graficar_lingadas_por_estiba(lingadas, resultado_final, estibas, nombre_archivo="grafico_lingadas.png"):

    conteo_inicial = Counter()
    for estiba in estibas:
        conteo_inicial[estiba.nombre] += len(estiba.lingadas)

    conteo_final = Counter()
    for i, estiba_id, nivel in resultado_final:
        estiba_nombre = next(e.nombre for e in estibas if e.id == estiba_id)
        conteo_final[estiba_nombre] += 1

    estibas_nombres = sorted(set(conteo_inicial.keys()).union(conteo_final.keys()))

    valores_antes = [conteo_inicial.get(estiba, 0) for estiba in estibas_nombres]
    valores_despues = [conteo_final.get(estiba, 0) for estiba in estibas_nombres]

    x = range(len(estibas_nombres))

    plt.figure(figsize=(14, 6))

    plt.bar(x, valores_antes, label='Lingadas ya asignadas (antes)', color='red')
    plt.bar(x, valores_despues, bottom=valores_antes, label='Nuevas asignaciones', color='yellow')

    for i in range(len(estibas_nombres)):
        total = valores_antes[i] + valores_despues[i]
        if valores_antes[i] > 0:
            plt.text(i, valores_antes[i]/2, str(valores_antes[i]), ha='center', va='center', fontsize=8)
        if valores_despues[i] > 0:
            plt.text(i, valores_antes[i] + valores_despues[i]/2, str(valores_despues[i]), ha='center', va='center', fontsize=8)
        if total > 0:
            plt.text(i, total + 0.3, str(total), ha='center', va='bottom', fontsize=9, fontweight='bold')

    plt.xticks(x, estibas_nombres, rotation=90)
    plt.xlabel("Estibas")
    plt.ylabel("Cantidad de lingadas")
    plt.title("Asignación de lingadas por estiba: antes vs después")
    plt.legend()
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.4)
    plt.ylim(0, 40)

    plt.savefig(nombre_archivo)

    try:
        os.startfile(nombre_archivo)
    except AttributeError:
        subprocess.run(["open" if sys.platform == "darwin" else "xdg-open", nombre_archivo])
    
    plt.close()
