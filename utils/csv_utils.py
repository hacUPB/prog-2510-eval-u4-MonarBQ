import matplotlib.pyplot as plt
import csv

def mostrar_primeras_filas(ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            
            filas_mostradas = 0
            print("Primeras filas del archivo:")
            for fila in csv_reader:
                print(fila)
                filas_mostradas += 1
                if filas_mostradas >= 15:
                    break
            
            if filas_mostradas == 0:
                print("El archivo está vacío.")
            elif filas_mostradas < 15:
                print(f"El archivo solo contiene {filas_mostradas} filas.")
                
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta '{ruta}'")
    except Exception as e:
        print("Error al mostrar filas:", e)

def calcular_estadisticas(ruta, columna):
    try:
        datos = []
        
        with open(ruta, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            
            if csv_reader.fieldnames and columna in csv_reader.fieldnames:
        
                for fila in csv_reader:
                    try:
                        if fila[columna].strip(): 
                            datos.append(float(fila[columna]))
                    except ValueError:
                        print(f"Advertencia: Valor no numérico '{fila[columna]}' ignorado.")
            else:
                print(f"Error: La columna '{columna}' no existe en el archivo.")
                return
    
        if datos:
            num_datos = len(datos)
            promedio = sum(datos) / num_datos
            datos_ordenados = sorted(datos)
            
            if num_datos % 2 == 1: 
                mediana = datos_ordenados[num_datos // 2]
            else:
                indice_medio = num_datos // 2
                mediana = (datos_ordenados[indice_medio - 1] + datos_ordenados[indice_medio]) / 2
            
            maximo = max(datos)
            minimo = min(datos)
            
            print(f"\nEstadísticas para la columna '{columna}':")
            print(f"Número de datos: {num_datos}")
            print(f"Promedio: {promedio:.4f}")
            print(f"Mediana: {mediana:.4f}")
            print(f"Valor máximo: {maximo}")
            print(f"Valor mínimo: {minimo}")
        else:
            print(f"No hay datos numéricos válidos en la columna '{columna}'.")
            
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta '{ruta}'")
    except Exception as e:
        print("Error al calcular estadísticas:", e)

def graficar_columna(ruta, columna):
    try:
        datos = []
        
        with open(ruta, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            
            if csv_reader.fieldnames and columna in csv_reader.fieldnames:
                for fila in csv_reader:
                    try:
                        if fila[columna].strip():
                            datos.append(float(fila[columna]))
                    except ValueError:
                        print(f"Advertencia: Valor no numérico '{fila[columna]}' ignorado.")
            else:
                print(f"Error: La columna '{columna}' no existe en el archivo.")
                return
        
        if datos:
            plt.figure(figsize=(10, 6)) 
            plt.plot(range(len(datos)), datos, 'b-', marker='o')  
            plt.title(f'Gráfica de la columna: {columna}')
            plt.xlabel('Índice')
            plt.ylabel(columna)
            plt.grid(True)  
            plt.tight_layout()  
            plt.show()
        else:
            print(f"No hay datos numéricos válidos para graficar en la columna '{columna}'.")
            
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta '{ruta}'")
    except Exception as e:
        print("Error al graficar la columna:", e)

def procesar_csv(ruta):
    try:
        try:
            with open(ruta, 'r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                encabezados = next(csv_reader, None)
                if not encabezados:
                    print("Error: El archivo CSV está vacío o no tiene formato válido.")
                    return
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en la ruta '{ruta}'")
            return
        except Exception as e:
            print(f"Error al abrir el archivo CSV: {e}")
            return
        
        while True:
            print("\nSubmenú para archivos CSV (.csv):")
            print("1. Mostrar las 15 primeras filas")
            print("2. Calcular Estadísticas")
            print("3. Graficar una columna")
            print("4. Volver al menú principal")
            
            opcion = input("Selecciona una opción: ")
            
            if opcion == "1":
                mostrar_primeras_filas(ruta)
            elif opcion == "2":
                with open(ruta, 'r', encoding='utf-8') as file:
                    csv_reader = csv.DictReader(file)
                    if csv_reader.fieldnames:
                        print("\nColumnas disponibles:", ", ".join(csv_reader.fieldnames))
                
                columna = input("Ingrese el nombre de la columna: ")
                calcular_estadisticas(ruta, columna)
            elif opcion == "3":
                with open(ruta, 'r', encoding='utf-8') as file:
                    csv_reader = csv.DictReader(file)
                    if csv_reader.fieldnames:
                        print("\nColumnas disponibles:", ", ".join(csv_reader.fieldnames))
                
                columna = input("Ingrese el nombre de la columna numérica: ")
                graficar_columna(ruta, columna)
            elif opcion == "4":
                break
            else:
                print("Opción inválida. Intente nuevamente.")
    except Exception as e:
        print("Error al procesar el archivo CSV:", e)