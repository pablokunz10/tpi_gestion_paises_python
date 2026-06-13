#Módulo encargado de la gestión básica de paises: agregar, actualizar y buscar

def agregar_pais(paises):
    
    # Solicita al usuario los datos de un nuevo pais y lo agrega a la lista
    # No permite campos vacios
    
    nombre = input("Nombre del país: ").strip()
    while nombre == "":
        print("El nombre no puede estar vacío.")
        nombre = input("Nombre del país: ").strip()

    poblacion = pedir_entero("Población: ")
    superficie = pedir_entero("Superficie (km²): ")

    continente = input("Continente: ").strip()
    while continente == "":
        print("El continente no puede estar vacío.")
        continente = input("Continente: ").strip()

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)
    print(f"País '{nombre}' agregado correctamente.")


def pedir_entero(mensaje):
   
    # Pide un número entero al usuario, validando que sea correcto y mayor o igual a 0
    
    while True:
        valor = input(mensaje).strip()
        try:
            numero = int(valor)
            if numero < 0:
                print("El valor no puede ser negativo.")
                continue
            return numero
        except ValueError:
            print("Debe ingresar un número entero válido.")


def buscar_pais(paises):
    
    # Busca países por nombre, permitiendo coincidencia parcial o exacta
    # Muestra los resultados encontrados
    
    if not paises:
        print("No hay países cargados.")
        return

    texto = input("Ingrese el nombre (o parte del nombre) a buscar: ").strip().lower()

    encontrados = [p for p in paises if texto in p["nombre"].lower()]

    if not encontrados:
        print("No se encontraron países que coincidan con la búsqueda.")
        return

    print(f"\nSe encontraron {len(encontrados)} país/es:")
    for pais in encontrados:
        mostrar_pais(pais)


def actualizar_pais(paises):
    
    #Permite actualizar la población y/o superficie de un pais, buscado por nombre exacto
    
    if not paises:
        print("No hay países cargados.")
        return

    nombre = input("Ingrese el nombre exacto del país a actualizar: ").strip()

    pais_encontrado = None
    for p in paises:
        if p["nombre"].lower() == nombre.lower():
            pais_encontrado = p
            break

    if pais_encontrado is None:
        print("No se encontró un país con ese nombre.")
        return

    print("Datos actuales:")
    mostrar_pais(pais_encontrado)

    nueva_poblacion = pedir_entero("Nueva población: ")
    nueva_superficie = pedir_entero("Nueva superficie (km²): ")

    pais_encontrado["poblacion"] = nueva_poblacion
    pais_encontrado["superficie"] = nueva_superficie

    print("Datos actualizados correctamente.")


def mostrar_pais(pais):
    
    # Muestra los datos de un pais de forma legible
    
    print(f"- {pais['nombre']} | Población: {pais['poblacion']} | "
          f"Superficie: {pais['superficie']} km² | Continente: {pais['continente']}")


def mostrar_lista_paises(paises):
    
    # Muestra todos los paises de la lista
    
    if not paises:
        print("No hay países cargados.")
        return

    for pais in paises:
        mostrar_pais(pais)
