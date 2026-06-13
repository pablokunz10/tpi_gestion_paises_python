#Módulo encargado de filtrar y ordenar la lista de paises segun distintos criterios

import unicodedata
from gestion import mostrar_pais, pedir_entero


def quitar_tildes(texto):
    
    #Quita las tildes de un texto, para poder comparar sin importar si el usuario las escribe o no

    normalizado = unicodedata.normalize("NFD", texto)
    return "".join(c for c in normalizado if unicodedata.category(c) != "Mn")


def filtrar_por_continente(paises):
    
    #Filtra y muestra los paises que pertenecen a un continente dado
    #No distingue mayusculas/minusculas ni tildes
    
    if not paises:
        print("No hay países cargados.")
        return

    continente = input("Ingrese el continente a filtrar: ").strip().lower()
    continente = quitar_tildes(continente)

    resultado = [
        p for p in paises
        if quitar_tildes(p["continente"].lower()) == continente
    ]

    if not resultado:
        print("No se encontraron países en ese continente.")
        return

    print(f"\nPaíses en {continente.capitalize()}:")
    for pais in resultado:
        mostrar_pais(pais)


def filtrar_por_rango_poblacion(paises):
    
    #Filtra y muestra los paises cuya población esta dentro de un rango dado
    
    if not paises:
        print("No hay países cargados.")
        return

    minimo = pedir_entero("Población mínima: ")
    maximo = pedir_entero("Población máxima: ")

    if minimo > maximo:
        print("El valor mínimo no puede ser mayor que el máximo.")
        return

    resultado = [p for p in paises if minimo <= p["poblacion"] <= maximo]

    if not resultado:
        print("No se encontraron países en ese rango de población.")
        return

    print("\nPaíses encontrados:")
    for pais in resultado:
        mostrar_pais(pais)


def filtrar_por_rango_superficie(paises):
    
    #Filtra y muestra los paises cuya superficie esta dentro de un rango dado
    
    if not paises:
        print("No hay países cargados.")
        return

    minimo = pedir_entero("Superficie mínima (km²): ")
    maximo = pedir_entero("Superficie máxima (km²): ")

    if minimo > maximo:
        print("El valor mínimo no puede ser mayor que el máximo.")
        return

    resultado = [p for p in paises if minimo <= p["superficie"] <= maximo]

    if not resultado:
        print("No se encontraron países en ese rango de superficie.")
        return

    print("\nPaíses encontrados:")
    for pais in resultado:
        mostrar_pais(pais)


def ordenar_paises(paises):
    
    # Ordena la lista de paises según el criterio elegido por el usuario:
    # nombre, población o superficie. Permite orden ascendente o descendente
    
    if not paises:
        print("No hay países cargados.")
        return

    print("\nOrdenar por:")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")

    opcion = input("Seleccione una opción: ").strip()

    criterios = {
        "1": "nombre",
        "2": "poblacion",
        "3": "superficie"
    }

    if opcion not in criterios:
        print("Opción inválida.")
        return

    orden = input("Orden (A = ascendente, D = descendente): ").strip().upper()

    if orden not in ("A", "D"):
        print("Opción de orden inválida.")
        return

    clave = criterios[opcion]
    reverso = (orden == "D")

    paises_ordenados = sorted(paises, key=lambda p: p[clave], reverse=reverso)

    print("\nPaíses ordenados:")
    for pais in paises_ordenados:
        mostrar_pais(pais)
