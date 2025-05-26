import random
from config import *

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

import csv
from datetime import datetime

class Lingada:
    def __init__(self, id, orden, colada, producto, fecha_salida, volumen, centro_origen, centro_destino):
        self.id = id
        self.orden = orden
        self.colada = colada
        self.producto = producto
        self.fecha_salida = fecha_salida
        self.volumen = volumen
        self.centro_origen = centro_origen
        self.centro_destino = centro_destino

    def __repr__(self):
        return (f"Lingada(id={self.id}, orden={self.orden}, colada={self.colada}, "
                f"producto={self.producto}, fecha_salida={self.fecha_salida}, volumen={self.volumen}, "
                f"centro_origen={self.centro_origen}, centro_destino={self.centro_destino})")

def cargar_lingadas_desde_txt(path_archivo):
    lingadas = []

    with open(path_archivo, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo, delimiter='|')
        for i, fila in enumerate(lector):
            try:
                lingada = Lingada(
                    id=i,
                    orden=fila["WORKORDER"],
                    colada=fila["HEAT"],
                    producto=fila["PRODUCT_ID"],
                    fecha_salida=datetime.strptime(fila["FINISH_DATE_MOV"], "%d/%m/%Y. %H:%M:%S"),
                    volumen=float(fila["OUT_DIAMETER"]) if fila["OUT_DIAMETER"] else 0.0,
                    centro_origen=fila["CENTRO"],
                    centro_destino=fila["CENTROSIG"]
                )
                lingadas.append(lingada)
                print(f"Lingada {i}: {lingada}")
            except Exception as e:
                print(f"Error en la fila {i}: {e}")

    print(f"\nTotal de lingadas cargadas: {len(lingadas)}")
    return lingadas

if __name__ == "__main__":
  archivo_path = r"datos\muestra-lingadas.txt"
  lingadas = cargar_lingadas_desde_txt(archivo_path)
