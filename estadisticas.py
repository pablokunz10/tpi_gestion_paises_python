
# Modulo encargado de calcular estadísticas sobre la lista de paises



def pais_mayor_poblacion(paises):
    
    # Devuelve el país con mayor poblacion
    
    return max(paises, key=lambda p: p["poblacion"])


def pais_menor_poblacion(paises):
    
    # Devuelve el pais con menor poblacion
    
    return min(paises, key=lambda p: p["poblacion"])


def promedio_poblacion(paises):
    
    #Calcula el promedio de población de todos los paises
    
    total = sum(p["poblacion"] for p in paises)
    return total / len(paises)


def promedio_superficie(paises):
    
    # Calcula el promedio de superficie de todos los paises
    
    total = sum(p["superficie"] for p in paises)
    return total / len(paises)


def cantidad_por_continente(paises):
    
    # Devuelve un diccionario con la cantidad de paises por continente
    
    conteo = {}
    for pais in paises:
        continente = pais["continente"]
        if continente in conteo:
            conteo[continente] += 1
        else:
            conteo[continente] = 1
    return conteo


def mostrar_estadisticas(paises):
    
    # Calcula y muestra todas las estadísticas pedidas por el TP
    
    if not paises:
        print("No hay países cargados para calcular estadísticas.")
        return

    mayor = pais_mayor_poblacion(paises)
    menor = pais_menor_poblacion(paises)
    prom_pob = promedio_poblacion(paises)
    prom_sup = promedio_superficie(paises)
    conteo = cantidad_por_continente(paises)

    print("\n--- ESTADÍSTICAS ---")
    print(f"País con mayor población: {mayor['nombre']} ({mayor['poblacion']} hab.)")
    print(f"País con menor población: {menor['nombre']} ({menor['poblacion']} hab.)")
    print(f"Promedio de población: {prom_pob:.2f} hab.")
    print(f"Promedio de superficie: {prom_sup:.2f} km²")
    print("\nCantidad de países por continente:")
    for continente, cantidad in conteo.items():
        print(f"  {continente}: {cantidad}")
