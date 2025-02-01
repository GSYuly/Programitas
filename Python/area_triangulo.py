def area_triangulo(base, altura):
    """Calcula el área de un triángulo."""
    return (base * altura) / 2

base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area = area_triangulo(base, altura)
print(f"El área del triángulo es: {area}")
