import random
from config import *
import pandas as pd
from lingadas import Lingada

# ------------------------------------------
# CARGA DE ESTIBAS
# ------------------------------------------

estibas = [{
    "id": j,
    "capacidad": 5.0,
    "ubicacion": random.randint(1, 5)
} for j in range(NUM_ESTIBAS)]

class Estiba:
    def __init__(self, nombre, x, y):
        self.nombre = nombre
        self.x = float(x)
        self.y = float(y)
        self.ubicacion = (self.x, self.y)
        self.lingadas = []

    def agregar_lingada(self, lingada):
        self.lingadas.append(lingada)

    def __repr__(self):
        return f"Estiba({self.nombre}, ({self.x},{self.y}), lingadas={len(self.lingadas)})"


def fila_vacia(fila):
    campos_clave = ["COLADA", "PRODUCTO", "PIEZAS", "DIAMETRO", "ESPESOR", "TONS", "LINGADA"]
    for campo in campos_clave:
        valor = fila.get(campo)
        if pd.isna(valor):
            continue
        if isinstance(valor, str) and valor.strip() == "":
            continue
        try:
            if float(str(valor).replace(".", "").replace(",", ".")) != 0.0:
                return False
        except (ValueError, TypeError):
            return False
    return True


def cargar_estibas_con_lingadas_desde_excel(path_archivo, hoja="Estibas"):
    df = pd.read_excel(path_archivo, sheet_name=hoja, dtype=str)
    estibas_dict = {}

    for _, fila in df.iterrows():
        estiba_nombre = fila["ESTIBA"]

        if estiba_nombre not in estibas_dict:
            try:
                x = float(str(fila["X"]).replace(",", "."))
                y = float(str(fila["Y"]).replace(",", "."))
            except Exception as e:
                print(f"Error en coordenadas de estiba {estiba_nombre}: {e}")
                x, y = 0.0, 0.0
            estibas_dict[estiba_nombre] = Estiba(estiba_nombre, x, y)

        if fila_vacia(fila):
            continue

        try:
            lingada = Lingada(
                id=fila["LINGADA"],
                estiba_nombre=fila["ESTIBA"],
                nivel=fila["NIVEL"],
                orden=fila["OP"],
                estado=fila["ESTADO"],
                colada=fila["COLADA"],
                producto=fila["PRODUCTO"],
                piezas=fila["PIEZAS"],
                acero=fila["ACERO"],
                diametro=float(fila["DIAMETRO"]) if not pd.isna(fila["DIAMETRO"]) else 0.0,
                fecha_stock=pd.to_datetime(fila["FCH_STOCK"], dayfirst=True, errors='coerce')               
            )
            estibas_dict[estiba_nombre].agregar_lingada(lingada)
        except Exception as e:
            print(f"Error al procesar lingada en estiba {estiba_nombre}: {e}")

    estibas = list(estibas_dict.values())

    for estiba in estibas:
        print(f"{estiba.nombre} → {len(estiba.lingadas)} lingadas @ {estiba.ubicacion}")
        for lingada in estiba.lingadas:
            print(f"  {lingada}")

    return estibas


# Ejemplo de uso
if __name__ == "__main__":
    archivo_estibas = r"datos.xlsx"
    cargar_estibas_con_lingadas_desde_excel(archivo_estibas)
