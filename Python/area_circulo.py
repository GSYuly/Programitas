def area_triangulo():
    """Calcula el área de un triángulo."""
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area1 = (base*altura)/2
    print("El área del triángulo es: ", area1)

def circulo():
    """Calcula el área de un triángulo."""
    radio = float(input("Ingrese el radio del circulo: "))
    area = 3.1416 *(radio*radio)
    print(f"El área del circulo es: ", area)

print("1= Area_triangulo")
print("2= Circulo")
opcion=int(input("SELECCIONA UNA OPCION: "))
if opcion == 1:
        area_triangulo()
if opcion == 2:
        circulo()




