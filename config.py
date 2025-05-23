# ------------------------------------------
# CONFIGURACIÓN GENERAL Y PARÁMETROS
# ------------------------------------------

NUM_LINGADAS = 100
NUM_ESTIBAS = 40
MAX_NIVELES = 5

# PESOS DE FUNCIÓN DE APTITUD
N1 = 10  # Igualdad de orden, colada, producto
N2 = 15  # Penalización por obstrucción
N3 = 8   # Lingada grande en estiba vacía
N4 = 6   # Lingada pequeña en estiba llena
N5 = 30  # Penalización por sobrecapacidad
N6 = 10  # Puntaje por cercanía a centro siguiente
N7 = 10  # Puntaje por ubicación respecto a origen/destino