# Inicializa la lista para almacenar los números
numbers = []

# Pide al usuario que ingrese números hasta que ingrese 0
print("Enter a list of numbers, type 0 when finished.")
while True:
    num = float(input("Enter number: "))
    if num == 0:
        break
    numbers.append(num)

# Calcula la suma de los números
total = sum(numbers)

# Calcula el promedio
average = total / len(numbers) if numbers else 0

# Encuentra el número máximo
largest = max(numbers) if numbers else None

# Encuentra el número positivo más pequeño
smallest_positive = min((num for num in numbers if num > 0), default=None)

# Ordena la lista
sorted_numbers = sorted(numbers)

# Imprime los resultados
print(f"The sum is: {total}")
print(f"The average is: {average}")
print(f"The largest number is: {largest}")
if smallest_positive is not None:
    print(f"The smallest positive number is: {smallest_positive}")
print("The sorted list is:")
for number in sorted_numbers:
    print(number)
