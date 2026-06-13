#Modulo encargado de la lectura y escritura del archivo CSV que contiene los datos de los paises

import csv

def cargar_paises(nombre_archivo):
    
    # Lee el archivo CSV y devuelve una lista de diccionarios, cada uno representando un pais
    # Si el archivo no existe o tiene errores de formato, devuelve lista vacia
   
    paises = []
    try:
        with open(nombre_archivo, "r", newline="", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip()
                    }
                    paises.append(pais)
                except (ValueError, KeyError):
                    print(f"Aviso: se ignoró una fila con formato inválido: {fila}")
    except FileNotFoundError:
        print(f"No se encontró el archivo '{nombre_archivo}'. Se inicia con lista vacía.")
    except Exception as e:
        print(f"Error inesperado al leer el archivo: {e}")

    return paises

def guardar_paises(nombre_archivo, paises):

    # Guarda la lista de paises en el archivo CSV, sobrescribiendo su contenido

    try:
        with open(nombre_archivo, "w", newline="", encoding="utf-8") as f:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()
            for pais in paises:
                escritor.writerow(pais)
        print("Datos guardados correctamente.")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
