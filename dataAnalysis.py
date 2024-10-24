import csv

# Cargar el conjunto de datos
filename = 'life-expectancy.csv'
data = []

with open(filename, mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Saltar la cabecera
    for row in csv_reader:
        data.append(row)

# Variables para encontrar la esperanza de vida más baja y más alta
min_life_expectancy = float('inf')
max_life_expectancy = float('-inf')

# Iterar a través de las filas de datos
for row in data:
    # Asegurarse de que los datos se puedan convertir a un número
    try:
        life_expectancy = float(row[3])  # Suponiendo que la esperanza de vida está en la cuarta columna
        # Encontrar el valor más bajo
        if life_expectancy < min_life_expectancy:
            min_life_expectancy = life_expectancy
        # Encontrar el valor más alto
        if life_expectancy > max_life_expectancy:
            max_life_expectancy = life_expectancy
    except ValueError:
        # Manejo de valores que no se pueden convertir a float
        continue

# Mostrar los resultados
print(f"La esperanza de vida más baja es: {min_life_expectancy}")
print(f"La esperanza de vida más alta es: {max_life_expectancy}")
