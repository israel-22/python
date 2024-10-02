# Solicitar al usuario su porcentaje de calificación
calificacion = int(input("Por favor, ingresa tu porcentaje de calificación: "))

# Inicializar la variable letter
letter = ""

# Determinar la calificación de letra
if calificacion >= 90:
    letter = "A"
elif calificacion >= 80:
    letter = "B"
elif calificacion >= 70:
    letter = "C"
elif calificacion >= 60:
    letter = "D"
else:
    letter = "F"

# Verificar si el usuario pasó el curso
if calificacion >= 70:
    print("¡Felicidades! Has pasado el curso.")
else:
    print("No has pasado el curso. ¡Sigue intentándolo!")

# Mostrar la calificación de letra
print(f"Tu calificación es: {letter}")

# Agregar signo + o - según el último dígito
ultimo_digito = calificacion % 10
signo = ""

# Verificar los signos solo para las letras A, B, C y D
if letter in ["A", "B", "C", "D"]:
    if ultimo_digito >= 7:
        signo = "+"
    elif ultimo_digito < 3:
        signo = "-"
    
# Ajustar el grado final para A y F
if letter == "A" and signo == "+":
    sign = ""
elif letter == "F":
    signo = ""

# Mostrar la calificación con signo
if signo:
    print(f"Tu calificación es: {letter}{signo}")
else:
    print(f"Tu calificación es: {letter}")
