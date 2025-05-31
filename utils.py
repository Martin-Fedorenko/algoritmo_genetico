from config import *
from carga_datos import *
import matplotlib.pyplot as plt
import random
from collections import Counter


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
    plt.show(block=False)
    plt.ylabel("Fitness")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def graficar_lingadas_por_estiba(lingadas, resultado_final):
    import matplotlib.pyplot as plt
    from collections import Counter

    # Conteo inicial por nombre de estiba (antes)
    conteo_inicial = Counter()
    for estiba in estibas:
        conteo_inicial[estiba.nombre] += len(estiba.lingadas)

    # Conteo final por nombre de estiba (nuevas asignaciones)
    conteo_final = Counter()
    for i, estiba_id, nivel in resultado_final:
        estiba_nombre = next(e.nombre for e in estibas if e.id == estiba_id)
        conteo_final[estiba_nombre] += 1

    # Unir todas las estibas involucradas
    estibas_nombres = sorted(set(conteo_inicial.keys()).union(conteo_final.keys()))

    # Valores para el gráfico
    valores_antes = [conteo_inicial.get(estiba, 0) for estiba in estibas_nombres]
    valores_despues = [conteo_final.get(estiba, 0) for estiba in estibas_nombres]

    x = range(len(estibas_nombres))

    # Crear la figura
    plt.figure(figsize=(14, 6))

    # Barras apiladas
    barras_antes = plt.bar(x, valores_antes, label='Lingadas ya asignadas (antes)', color='red')
    barras_despues = plt.bar(x, valores_despues, bottom=valores_antes, label='Nuevas asignaciones', color='yellow')

    # Agregar etiquetas en cada barra
    for i in range(len(estibas_nombres)):
        total = valores_antes[i] + valores_despues[i]

        if valores_antes[i] > 0:
            plt.text(i, valores_antes[i]/2, str(valores_antes[i]), ha='center', va='center', fontsize=8)
        if valores_despues[i] > 0:
            plt.text(i, valores_antes[i] + valores_despues[i]/2, str(valores_despues[i]), ha='center', va='center', fontsize=8)
        if total > 0:
            plt.text(i, total + 0.3, str(total), ha='center', va='bottom', fontsize=9, fontweight='bold')

    # Etiquetas y formato
    plt.xticks(x, estibas_nombres, rotation=90)
    plt.xlabel("Estibas")
    plt.ylabel("Cantidad de lingadas")
    plt.title("Asignación de lingadas por estiba: antes vs después")
    plt.legend()
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.4)

    plt.ylim(0, 40)  # Limitar el eje Y hasta 40

    plt.show(block=False)
