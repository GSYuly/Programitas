def calcular_area_cuadrado():
    lado = float(input("Ingresa la longitud del lado del cuadrado: "))
    return lado ** 2

def calcular_area_rectangulo():
    base = float(input("Ingresa la base del rectángulo: "))
    altura = float(input("Ingresa la altura del rectángulo: "))
    return base * altura

def calcular_area_trapecio():
    base_mayor = float(input("Ingresa la base mayor del trapecio: "))
    base_menor = float(input("Ingresa la base menor del trapecio: "))
    altura = float(input("Ingresa la altura del trapecio: "))
    return ((base_mayor + base_menor) * altura) / 2

def area_triangulo():
    """Calcula el área de un triángulo."""
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    return ((base*altura)/2)

def circulo():
    """Calcula el área de un triángulo."""
    radio = float(input("Ingrese el radio del circulo: "))
    return (3.1416 *(radio*radio))

def main():
    while True:
        print("\nCalculadora de Áreas")
        print("1. Calcular el área de un cuadrado")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un trapecio")
        print("4. Calcular el área de un triangulo")
        print("5. Calcular el área de un Circulo")
        print("6. Salir")

        opcion = input("Selecciona una opción (1-6): ")

        if opcion == "1":
            area = calcular_area_cuadrado()
            print(f"El área del cuadrado es: {area}")
        elif opcion == "2":
            area = calcular_area_rectangulo()
            print(f"El área del rectángulo es: {area}")
        elif opcion == "3":
            area = calcular_area_trapecio()
            print(f"El área del trapecio es: {area}")
        elif opcion == "4":
            area = area_triangulo()
            print(f"El área del triangulo es: {area}")
        elif opcion == "5":
            area = circulo()
            print(f"El área del circulo es: {area}")
        elif opcion == "6":
            print("Saliendo del programa. ¡Adiós :D!")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo :).")

if __name__ == "__main__":
    main()
