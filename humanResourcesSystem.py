# Definimos la función principal para el programa de Recursos Humanos
def main():
    # Abrimos el archivo de texto que contiene la información de los empleados
    with open("hr_system.txt", "r") as file:
        for line in file:
            # Eliminamos espacios en blanco al principio y al final de la línea
            line = line.strip()
            # Dividimos la línea en partes
            parts = line.split(" ")
            
            # Asignamos los valores a las variables correspondientes
            name = parts[0]
            id_number = parts[1]
            job_title = parts[2]
            salary = float(parts[3])
            
            # Calculamos el monto del cheque de pago (salario mensual / 2)
            paycheck_amount = (salary / 12) * 2
            
            # Si el empleado es ingeniero, agregamos una bonificación de $1000
            if job_title.lower() == "engineer":
                paycheck_amount += 1000
            
            # Mostramos la información formateada en la pantalla
            print(f"{name} (ID: {id_number}), {job_title} - ${paycheck_amount:.2f}")

# Ejecutamos la función principal
if __name__ == "__main__":
    main()

