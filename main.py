import os
from utils.file_utils import listar_archivos, procesar_txt, procesar_csv

def main():
    while True:
        print("\nMenú Principal:")
        print("1. Listar archivos presentes en la ruta actual")
        print("2. Procesar archivo de texto (.txt)")
        print("3. Procesar archivo separado por comas (.csv)")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            ruta = input("Ingrese la ruta o deje vacío para la actual: ")
            if not ruta:
                ruta = os.getcwd()
            listar_archivos(ruta)
        elif opcion == "2":
            ruta = input("Ingrese la ruta del archivo .txt: ")
            procesar_txt(ruta)
        elif opcion == "3":
            ruta = input("Ingrese la ruta del archivo .csv: ")
            procesar_csv(ruta)
        elif opcion == "4":
            print("Saliendo de la aplicación...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()