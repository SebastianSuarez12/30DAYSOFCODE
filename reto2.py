# Integrantes -> Sebastián Suárez, Steven Erazo

def centimetros_a_pulgadas(centimetros):
    return centimetros * 0.393701

def pulgadas_a_centimetros(pulgadas):
    return pulgadas * 2.54

def kilometros_a_millas(kilometros):
    return kilometros * 0.621371

def millas_a_kilometros(millas):
    return millas * 1.60934

# Menú de opciones
def menu():
    print("1. Convertir centímetros a pulgadas")
    print("2. Convertir pulgadas a centímetros")
    print("3. Convertir kilómetros a millas")
    print("4. Convertir millas a kilómetros")
    print("5. Salir")

# Función principal
def main():
    while True:
        menu()
        opcion = input("\nSelecciona una opción (1-5): ")

        if opcion == "1":
            centimetros = float(input("Ingresa la longitud en centímetros: "))
            pulgadas = centimetros_a_pulgadas(centimetros)
            print(f"{centimetros} centímetros equivalen a {pulgadas} pulgadas.\n")
        elif opcion == "2":
            pulgadas = float(input("Ingresa la longitud en pulgadas: "))
            centimetros = pulgadas_a_centimetros(pulgadas)
            print(f"{pulgadas} pulgadas equivalen a {centimetros} centímetros.\n")
        elif opcion == "3":
            kilometros = float(input("Ingresa la longitud en kilómetros: "))
            millas = kilometros_a_millas(kilometros)
            print(f"{kilometros} kilómetros equivalen a {millas} millas.\n")
        elif opcion == "4":
            millas = float(input("Ingresa la longitud en millas: "))
            kilometros = millas_a_kilometros(millas)
            print(f"{millas} millas equivalen a {kilometros} kilómetros.\n")
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.\n")


main()
