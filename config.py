# ------------------------------------------
# CONFIGURACIÓN GENERAL Y PARÁMETROS
# ------------------------------------------

ARCHIVO_DATOS = r"datos_originales.xlsx"
HOJA_ESTIBAS = "Estibas"
HOJA_LINGADAS = "Lingadas"
MAX_NIVELES_ESTIBA = 32
LADO_ZONA_CENTRO = 50

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
N1 = 100 # Agrupamiento
N2 = 15  # Penalización por obstrucción
N3 = 8   # Cercania zona
N4 = 6   # Distancia estiba - (destino + origen)
N5 = 30  # Penalización por sobrecapacidad