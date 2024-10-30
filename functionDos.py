import math

# Función para calcular el área de un rectángulo
def compute_area_rectangle(length, width):
    return length * width

# Función para calcular el área de un cuadrado utilizando la función de área de rectángulo
def compute_area_square(side):
    return compute_area_rectangle(side, side)

# Función para calcular el área de un círculo
def compute_area_circle(radius):
    return math.pi * (radius ** 2)

# Bucle principal para preguntar al usuario el tipo de forma
while True:
    shape = input("Enter the shape (square, rectangle, circle) or type 'quit' to exit: ").lower()

    if shape == "quit":
        print("Exiting the program.")
        break
    elif shape == "square":
        side = float(input("Enter the side length of the square: "))
        area = compute_area_square(side)
        print(f"The area of the square is: {area}")
    elif shape == "rectangle":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = compute_area_rectangle(length, width)
        print(f"The area of the rectangle is: {area}")
    elif shape == "circle":
        radius = float(input("Enter the radius of the circle: "))
        area = compute_area_circle(radius)
        print(f"The area of the circle is: {area}")
    else:
        print("Invalid shape. Please enter 'square', 'rectangle', 'circle', or 'quit'.")
