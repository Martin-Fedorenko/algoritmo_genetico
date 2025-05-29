# ------------------------------------------
# CONFIGURACIÓN GENERAL Y PARÁMETROS
# ------------------------------------------

ARCHIVO_DATOS = r"datos.xlsx"
HOJA_ESTIBAS = "Estibas"
HOJA_LINGADAS = "Lingadas"
NUM_LINGADAS = 76
NUM_ESTIBAS = 68
MAX_NIVELES_ESTIBA = 32

# ------------------------------------------
# CARGA DE CENTROS
# ------------------------------------------

CENTROS = {
    "LIN1": (100, 100),
    "TRA2": (400, 300),
    "TRA3": (150, 200),
    "UTL3": (300, 100),
    "LAC2": (200, 200)
}


# PESOS DE FUNCIÓN DE APTITUD
N1 = 100 # Igualdad de orden, colada, producto
N2 = 15  # Penalización por obstrucción
N3 = 8   # Lingada grande en estiba vacía
N4 = 6   # Lingada pequeña en estiba llena
N5 = 30  # Penalización por sobrecapacidad
N6 = 10  # Puntaje por cercanía a centro siguiente
N7 = 10  # Puntaje por ubicación respecto a origen/destino