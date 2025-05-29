from config import *
import pandas as pd
from datetime import datetime

class Lingada:
    def __init__(self, id=None, orden=None, colada=None, producto=None,piezas=None, estado=None, acero=None,diametro=None, fecha_stock=None,estiba_nombre=None,centro_origen=None, centro_destino=None,status=None, inicial_date_prg=None, finish_date_prg=None):
        
        self.id = id
        self.orden = orden
        self.colada = colada
        self.producto = producto
        self.piezas = int(piezas) if piezas is not None else None
        self.estado = estado
        self.acero = acero
        self.diametro = float(str(diametro).replace(".", "").replace(",", ".")) if diametro else None
        self.fecha_stock = pd.to_datetime(fecha_stock, errors='coerce') if fecha_stock else None
        self.estiba_nombre = estiba_nombre
        self.centro_origen = centro_origen
        self.centro_destino = centro_destino
        self.status = status
        self.inicial_date_prg = pd.to_datetime(inicial_date_prg, errors='coerce') if inicial_date_prg else None
        self.finish_date_prg = pd.to_datetime(finish_date_prg, errors='coerce') if finish_date_prg else None

    def __repr__(self):
        return f"Lingada(id={self.id}, Orden={self.orden}, colada={self.colada}, producto={self.producto}, piezas={self.piezas})"