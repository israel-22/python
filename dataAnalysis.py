import csv
#----------------------
# For Santos Israel
#----------------------
# Program to analyze life expectancy data and find specific insights.
# The program loads data from a CSV file, calculates the minimum and maximum life expectancy,
# and allows users to input a year to get the average, minimum, and maximum life expectancy for that year.

# Load the dataset
#please check the filename in the path!!!!!!!!!======>
#filename = 'life-expectancy.csv' #<====== comented
filename = 'D:/Backup/Documentos/visualStudio/python/life-expectancy.csv'

data = []

with open(filename, mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Skip the header
    for row in csv_reader:
        data.append(row)

# Variables to find the lowest and highest life expectancy, including the associated year and country
min_life_expectancy = float('inf')
max_life_expectancy = float('-inf')
min_life_country = ""
min_life_year = ""
max_life_country = ""
max_life_year = ""

# Iterate through the data rows to find the overall min and max life expectancy
for row in data:
    # Ensure the data can be converted to a number
    try:
        life_expectancy = float(row[3])  # Assuming life expectancy is in the fourth column
        country = row[0]
        year = row[2]

        # Find the lowest value and its country/year
        if life_expectancy < min_life_expectancy:
            min_life_expectancy = life_expectancy
            min_life_country = country
            min_life_year = year

        # Find the highest value and its country/year
        if life_expectancy > max_life_expectancy:
            max_life_expectancy = life_expectancy
            max_life_country = country
            max_life_year = year
    except ValueError:
        # Handle values that cannot be converted to float
        continue

# Display the overall results
print(f"The overall max life expectancy is: {max_life_expectancy} from {max_life_country} in {max_life_year}")
print(f"The overall min life expectancy is: {min_life_expectancy} from {min_life_country} in {min_life_year}")

# Prompt the user to enter a year of interest
year_of_interest = input("Enter the year of interest: ")

# Variables for calculating average, min, and max for the specified year
total_life_expectancy = 0
count = 0
year_min_life_expectancy = float('inf')
year_max_life_expectancy = float('-inf')
year_min_country = ""
year_max_country = ""

# Iterate again to calculate average, min, and max for the specified year
for row in data:
    try:
        country = row[0]
        year = row[2]
        life_expectancy = float(row[3])

        # Process only the rows that match the specified year
        if year == year_of_interest:
            # Calculate the total for the average
            total_life_expectancy += life_expectancy
            count += 1

            # Check for minimum and maximum life expectancy for the year
            if life_expectancy < year_min_life_expectancy:
                year_min_life_expectancy = life_expectancy
                year_min_country = country

            if life_expectancy > year_max_life_expectancy:
                year_max_life_expectancy = life_expectancy
                year_max_country = country

    except ValueError:
        # Handle values that cannot be converted to float
        continue

# Calculate the average for the specified year
if count > 0:
    average_life_expectancy = total_life_expectancy / count
    print(f"For the year {year_of_interest}:")
    print(f"The average life expectancy across all countries was {average_life_expectancy:.2f}")
    print(f"The max life expectancy was in {year_max_country} with {year_max_life_expectancy}")
    print(f"The min life expectancy was in {year_min_country} with {year_min_life_expectancy}")
else:
    print(f"No data available for the year {year_of_interest}")
