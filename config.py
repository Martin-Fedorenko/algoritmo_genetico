# ------------------------------------------
# CONFIGURACIÓN GENERAL Y PARÁMETROS
# ------------------------------------------

ARCHIVO_DATOS = r"datos.xlsx"
HOJA_ESTIBAS = "Estibas"
HOJA_LINGADAS = "Lingadas"
NUM_LINGADAS = 77
NUM_ESTIBAS = 68
MAX_NIVELES_ESTIBA = 32

# PESOS DE FUNCIÓN DE APTITUD
N1 = 10  # Igualdad de orden, colada, producto
N2 = 15  # Penalización por obstrucción
N3 = 8   # Lingada grande en estiba vacía
N4 = 6   # Lingada pequeña en estiba llena
N5 = 30  # Penalización por sobrecapacidad
N6 = 10  # Puntaje por cercanía a centro siguiente
N7 = 10  # Puntaje por ubicación respecto a origen/destino