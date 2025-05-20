import matplotlib.pyplot as plt

def contar_palabras_y_caracteres(ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as file:
            contenido = file.read()
            palabras = contenido.split()
            num_palabras = len(palabras)
            num_caracteres = len(contenido)
            num_caracteres_sin_espacios = 0

            for palabra in palabras:
                num_caracteres_sin_espacios += len(palabra)

        print(f"Número de palabras: {num_palabras}")
        print(f"Número de caracteres (incluyendo espacios): {num_caracteres}")
        print(f"Número de caracteres (sin contar espacios): {num_caracteres_sin_espacios}")
    except Exception as e:
        print("Error al procesar el archivo:", e)


def reemplazar_palabra(ruta):
    try:
        palabra_a_reemplazar = input("Ingrese la palabra a buscar: ")
        nueva_palabra = input("Ingrese la nueva palabra: ")

        with open(ruta, 'r', encoding='utf-8') as file:
            contenido = file.read()

        contenido_nuevo = contenido.replace(palabra_a_reemplazar, nueva_palabra)

        with open(ruta, 'w', encoding='utf-8') as file:
            file.write(contenido_nuevo)

        print("Palabra reemplazada con éxito.")
    except Exception as e:
        print("Error al reemplazar palabra:", e)

def histograma_vocales(ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as file:
            contenido = file.read().lower()
            conteo_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

            for letra in contenido:
                if letra in conteo_vocales:
                    conteo_vocales[letra] += 1

#Graficar el histograma#

            plt.bar(conteo_vocales.keys(), conteo_vocales.values(), color='orange')
            plt.title('Histograma de Ocurrencia de Vocales')
            plt.xlabel('Vocales')
            plt.ylabel('Número de Ocurrencias')
            plt.show()
    except Exception as e:
        print("Error al generar el histograma:", e)

def procesar_txt(ruta):
    while True:
        print("\nSubmenú para archivos de texto (.txt):")
        print("1. Contar número de palabras y caracteres")
        print("2. Reemplazar una palabra por otra")
        print("3. Histograma de ocurrencia de las vocales")
        print("4. Volver al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            contar_palabras_y_caracteres(ruta)
        elif opcion == "2":
            reemplazar_palabra(ruta)
        elif opcion == "3":
            histograma_vocales(ruta)
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")
