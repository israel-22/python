# #if/else para colocar condiciones de uso explicar bien a Bryan

# color = input("What is your favorite color? ")

# # This if statement will only match "blue" not "Blue" or "BLUE"
# if color == "blue":
#     print("I like blue too.")

# # This if statement will match the word blue, regardless of the capitalization
# if color.lower() == "blue":
#     print("I like blue too.")


#//////////////////////////::::::::::::::::::::::::::::::://///////////
 #segundo caso en este pide igualdades y ademas un animal favorito

# Solicitar el primer número
first_number = int(input("What is the first number? "))

# Solicitar el segundo número
second_number = int(input("What is the second number? "))

# Comparar los números
if first_number > second_number:
    print("The first number is greater")
else:
    print("The first number is not greater")

if first_number == second_number:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

if second_number > first_number:
    print("The second number is greater")
else:
    print("The second number is not greater")

# Solicitar el animal favorito
favorite_animal = input("What is your favorite animal? ").lower()

# Comparar el animal favorito
if favorite_animal == "bear":
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")
