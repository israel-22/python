def evaluar_prestamo():
    # Solicitar la calificación para el tamaño del préstamo
    loan_size = int(input("¿Qué tan grande es el préstamo (1-10)? "))

    # Solicitar la calificación del historial de crédito
    credit_score = int(input("¿Qué tan bueno es su historial de crédito (1-10)? "))

    # Solicitar la calificación de ingresos
    income = int(input("¿Qué tan altos son sus ingresos (1-10)? "))

    # Solicitar la calificación del pago inicial
    down_payment = int(input("¿Qué tan grande es su pago inicial (1-10)? "))

    # Variable booleana para decidir si prestar o no
    should_loan = False

    # Reglas de decisión
    if loan_size >= 5:
        # Si el tamaño del préstamo es al menos 5
        if credit_score >= 7 and income >= 7:
            should_loan = True
        elif credit_score >= 7 or income >= 7:
            if down_payment >= 5:
                should_loan = True
            else:
                should_loan = False
        else:
            should_loan = False
    else:
        # Si el tamaño del préstamo es menor a 5
        if credit_score < 4:
            should_loan = False
        else:
            if income >= 7 or down_payment >= 7:
                should_loan = True
            elif income >= 4 and down_payment >= 4:
                should_loan = True
            else:
                should_loan = False

    # Mostrar el resultado al usuario
    if should_loan:
        print("Decisión: sí")
    else:
        print("Decisión: no")

# Ciclo para permitir reiniciar el programa
while True:
    evaluar_prestamo()
    
    # Preguntar si desea reiniciar o salir
    reiniciar = input("¿Deseas evaluar otro préstamo? (sí/no): ").lower()
    
    if reiniciar != "sí":
        print("¡Gracias por usar el evaluador de préstamos!")
        break
