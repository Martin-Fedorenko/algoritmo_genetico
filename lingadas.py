import random
from config import *
import pandas as pd
from datetime import datetime

# ------------------------------------------
# CARGA DE LINGADAS
# ------------------------------------------

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
import pandas as pd

class Lingada:
    def __init__(self, 
                 id=None, orden=None, colada=None, producto=None,
                 piezas=None, nivel=None, estado=None, acero=None,
                 diametro=None, fecha_stock=None,
                 estiba_nombre=None,
                 centro_origen=None, centro_destino=None,
                 status=None,
                 inicial_date_prg=None, finish_date_prg=None):
        
        self.id = id
        self.orden = orden
        self.colada = colada
        self.producto = producto
        self.piezas = int(piezas) if piezas is not None else None
        self.nivel = int(nivel) if nivel is not None else None
        self.estado = estado
        self.acero = acero
        self.diametro = float(str(diametro).replace(".", "").replace(",", ".")) if diametro else None
        self.fecha_stock = pd.to_datetime(fecha_stock, dayfirst=True, errors='coerce') if fecha_stock else None
        self.estiba_nombre = estiba_nombre
        self.centro_origen = centro_origen
        self.centro_destino = centro_destino
        self.status = status
        self.inicial_date_prg = pd.to_datetime(inicial_date_prg, dayfirst=True, errors='coerce') if inicial_date_prg else None
        self.finish_date_prg = pd.to_datetime(finish_date_prg, dayfirst=True, errors='coerce') if finish_date_prg else None

    def __repr__(self):
        return f"Lingada(id={self.id}, colada={self.colada}, producto={self.producto}, piezas={self.piezas})"

def cargar_lingadas_desde_excel(path_archivo, hoja="Lingadas"):
    lingadas = []
    df = pd.read_excel(path_archivo, sheet_name=hoja)

    for i, fila in df.iterrows():
        try:
            lingada = Lingada(
                id=i,
                orden=fila["WORKORDER"],
                colada=fila["HEAT"],
                producto=fila["PRODUCT_ID"],
                diametro=float(fila["OUT_DIAMETER"]) if not pd.isna(fila["OUT_DIAMETER"]) else 0.0,
                centro_origen=fila["CENTRO"],
                centro_destino=fila["CENTROSIG"],
                status=fila["STATUS"],
                piezas=fila["PIECES"],
                steel_grade_desc=fila["STEEL_GRADE_DESC"],
                inicial_date_prg=pd.to_datetime(fila["INICIAL_DATE_PRG"], dayfirst=True, errors='coerce'),
                finish_date_prg=pd.to_datetime(fila["FINISH_DATE_PRG"], dayfirst=True, errors='coerce')
            )
            print(f"  {lingada}")
            lingadas.append(lingada)
        except Exception as e:
            print(f"Error en fila {i}: {e}")

    print(f"\nTotal de lingadas cargadas desde '{hoja}': {len(lingadas)}")
    return lingadas


if __name__ == "__main__":
    archivo_path = r"datos.xlsx"
    lingadas = cargar_lingadas_desde_excel(archivo_path)
