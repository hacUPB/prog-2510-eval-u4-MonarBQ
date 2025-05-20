import os
from utils.text_utils import procesar_txt
from utils.csv_utils import procesar_csv
def listar_archivos(ruta):
    try:
        archivos = os.listdir(ruta)
        print("Archivos en la ruta:")
        for archivo in archivos:
            print(f"- {archivo}")
    except Exception as e:
        print("Error al listar archivos:", e)

def manejar_txt(ruta):
    procesar_txt(ruta)

def manejar_csv(ruta):
    procesar_csv(ruta)
