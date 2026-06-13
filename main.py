# Archivo principal del sistema de gestion de paises
# Contiene el menu y el flujo principal del programa


from archivos import cargar_paises, guardar_paises
from gestion import agregar_pais, buscar_pais, actualizar_pais, mostrar_lista_paises
from filtros_orden import (
    filtrar_por_continente,
    filtrar_por_rango_poblacion,
    filtrar_por_rango_superficie,
    ordenar_paises
)
from estadisticas import mostrar_estadisticas


NOMBRE_ARCHIVO = "paises.csv"


def mostrar_menu():
    
    # Muestra las opciones del menu principal
    
    print("\n===== GESTIÓN DE PAÍSES =====")
    print("1. Mostrar todos los países")
    print("2. Agregar país")
    print("3. Actualizar población y superficie de un país")
    print("4. Buscar país por nombre")
    print("5. Filtrar por continente")
    print("6. Filtrar por rango de población")
    print("7. Filtrar por rango de superficie")
    print("8. Ordenar países")
    print("9. Mostrar estadísticas")
    print("10. Guardar cambios en el archivo")
    print("0. Salir")


def main():
    
    # Función principal: carga los datos, ejecuta el menu y guarda los cambios al salir
    
    paises = cargar_paises(NOMBRE_ARCHIVO)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_lista_paises(paises)
        elif opcion == "2":
            agregar_pais(paises)
        elif opcion == "3":
            actualizar_pais(paises)
        elif opcion == "4":
            buscar_pais(paises)
        elif opcion == "5":
            filtrar_por_continente(paises)
        elif opcion == "6":
            filtrar_por_rango_poblacion(paises)
        elif opcion == "7":
            filtrar_por_rango_superficie(paises)
        elif opcion == "8":
            ordenar_paises(paises)
        elif opcion == "9":
            mostrar_estadisticas(paises)
        elif opcion == "10":
            guardar_paises(NOMBRE_ARCHIVO, paises)
        elif opcion == "0":
            guardar_paises(NOMBRE_ARCHIVO, paises)
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
