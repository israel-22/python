import csv

# Load the dataset
filename = 'life-expectancy.csv'
data = []

with open(filename, mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Skip the header
    for row in csv_reader:
        data.append(row)

# Variables to find the lowest and highest life expectancy
min_life_expectancy = float('inf')
max_life_expectancy = float('-inf')

# Iterate through the data rows
for row in data:
    # Ensure the data can be converted to a number
    try:
        life_expectancy = float(row[3])  # Assuming life expectancy is in the fourth column
        # Find the lowest value
        if life_expectancy < min_life_expectancy:
            min_life_expectancy = life_expectancy
        # Find the highest value
        if life_expectancy > max_life_expectancy:
            max_life_expectancy = life_expectancy
    except ValueError:
        # Handle values that cannot be converted to float
        continue

# Display the results
print(f"The lowest life expectancy is: {min_life_expectancy}")
print(f"The highest life expectancy is: {max_life_expectancy}")
