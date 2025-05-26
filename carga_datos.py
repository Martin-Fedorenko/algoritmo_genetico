from config import *
from lingada import *
from estiba import *

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

# ------------------------------------------
# CARGA DE ESTIBAS
# ------------------------------------------

def fila_vacia(fila):
    campos_clave = ["COLADA", "PRODUCTO", "PIEZAS", "DIAMETRO", "LINGADA"]
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


def cargar_estibas_con_lingadas_desde_excel(path_archivo, hoja):
    df = pd.read_excel(path_archivo, sheet_name=hoja, dtype=str)
    estibas_dict = {}
    i=0

    for _, fila in df.iterrows():

        estiba_nombre = fila["ESTIBA"]

        if estiba_nombre not in estibas_dict:
            try:
                x = float(str(fila["X"]).replace(",", "."))
                y = float(str(fila["Y"]).replace(",", "."))
            except Exception as e:
                print(f"Error en coordenadas de estiba {estiba_nombre}: {e}")
                x, y = 0.0, 0.0
            estibas_dict[estiba_nombre] = Estiba(i,estiba_nombre, x, y)
            i+=1

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

# ------------------------------------------
# CARGA DE LINGADAS
# ------------------------------------------

def cargar_lingadas_desde_excel(path_archivo, hoja):
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
                acero=fila["STEEL_GRADE_DESC"],
                inicial_date_prg=pd.to_datetime(fila["INICIAL_DATE_PRG"], dayfirst=True, errors='coerce'),
                finish_date_prg=pd.to_datetime(fila["FINISH_DATE_PRG"], dayfirst=True, errors='coerce')
            )
            print(f"  {lingada}")
            lingadas.append(lingada)
        except Exception as e:
            print(f"Error en fila {i}: {e}")

    print(f"\nTotal de lingadas cargadas desde '{hoja}': {len(lingadas)}")
    return lingadas




# ------------------------------------------
# CARGA INICIAL DE LINGADAS Y ESTIBAS
# ------------------------------------------


lingadas = cargar_lingadas_desde_excel(ARCHIVO_DATOS, HOJA_LINGADAS)
NUM_LINGADAS = len(lingadas)
estibas = cargar_estibas_con_lingadas_desde_excel(ARCHIVO_DATOS, HOJA_ESTIBAS)
NUM_ESTIBAS = len(estibas)