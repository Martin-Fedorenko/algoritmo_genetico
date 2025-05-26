import random
from config import *

# ------------------------------------------
# CARGA DE ESTIBAS
# ------------------------------------------

estibas = [{
    "id": j,
    "capacidad": 5.0,
    "ubicacion": random.randint(1, 5)
} for j in range(NUM_ESTIBAS)]

import csv
from datetime import datetime
from collections import defaultdict

class Lingada:
    def __init__(self, nivel, op, estado, colada, producto, lote, piezas, acero, diametro, espesor, ocupacion_stock,
                 ocupacion_estiba, fecha_stock, toneladas, codigo, en_uso, piezas_cargar):
        self.nivel = int(nivel)
        self.op = op
        self.estado = estado
        self.colada = colada
        self.producto = producto
        self.lote = lote
        self.piezas = int(piezas)
        self.acero = acero
        self.diametro = float(diametro)
        self.espesor = float(espesor)
        self.ocupacion_stock = float(ocupacion_stock)
        self.ocupacion_estiba = float(ocupacion_estiba)
        self.fecha_stock = datetime.strptime(fecha_stock, "%d/%m/%Y %H:%M:%S")
        self.toneladas = float(toneladas)
        self.codigo = codigo
        self.en_uso = en_uso
        self.piezas_cargar = int(piezas_cargar) if piezas_cargar else 0

    def __repr__(self):
        return f"Lingada({self.codigo}, piezas={self.piezas}, diam={self.diametro})"

class Estiba:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ubicacion = nombre  # Por ahora es igual al nombre
        self.lingadas = []

    def agregar_lingada(self, lingada):
        self.lingadas.append(lingada)

    def __repr__(self):
        return f"Estiba({self.nombre}, lingadas={len(self.lingadas)})"

def fila_vacia(fila):
    campos_clave = ["COLADA", "PRODUCTO", "PIEZAS", "DIAMETRO", "ESPESOR", "TONS", "LINGADA"]
    for campo in campos_clave:
        valor = fila.get(campo)
        if valor is None:
            continue
        if isinstance(valor, str) and valor == "":
            continue
        try:
            if float(valor) != 0.0:
                return False
        except (ValueError, TypeError):
            return False  # Si no se puede convertir a float, entonces no es un valor vacío
    return True


def cargar_estibas_con_lingadas(path_archivo):
    estibas_dict = defaultdict(lambda: Estiba(""))

    with open(path_archivo, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo, delimiter='|')
        for fila in lector:
            estiba_nombre = fila["ESTIBA"]
            if estiba_nombre not in estibas_dict:
                estibas_dict[estiba_nombre] = Estiba(estiba_nombre)

            if fila_vacia(fila):
                continue  # La estiba se mantiene, pero no se agrega una lingada

            try:
                lingada = Lingada(
                    nivel=fila["NIVEL"],
                    op=fila["OP"],
                    estado=fila["ESTADO"],
                    colada=fila["COLADA"],
                    producto=fila["PRODUCTO"],
                    lote=fila["LOTE"],
                    piezas=fila["PIEZAS"],
                    acero=fila["ACERO"],
                    diametro=fila["DIAMETRO"],
                    espesor=fila["ESPESOR"],
                    ocupacion_stock=fila["OCUPACION STOCK"],
                    ocupacion_estiba=fila["OCUPACION_ESTIBA"],
                    fecha_stock=fila["FCH_STOCK"],
                    toneladas=fila["TONS"],
                    codigo=fila["LINGADA"],
                    en_uso=fila["EN USO"],
                    piezas_cargar=fila["PZS CARGAR"]
                )
                estibas_dict[estiba_nombre].agregar_lingada(lingada)
            except Exception as e:
                print(f"Error en fila {fila}: {e}")

    estibas = list(estibas_dict.values())

    for estiba in estibas:
        print(f"{estiba.nombre} → {len(estiba.lingadas)} lingadas")
        for lingada in estiba.lingadas:
            print(f"  {lingada}")

    return estibas

# Ejemplo de uso
if __name__ == "__main__":
    archivo_estibas = r"datos\muestra-stock-inicial.txt"  # Ajustá el path según tu estructura
    cargar_estibas_con_lingadas(archivo_estibas)

