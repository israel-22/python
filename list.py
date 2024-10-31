# Creamos una lista vacía para almacenar los nombres de los amigos
friends = []

# Bucle que sigue pidiendo nombres hasta que el usuario ingrese "fin"
while True:
    friend = input("Type the name of a friend: ")

    # Verificamos si el usuario ha ingresado "fin"
    if friend.lower() == "fin":
        break
    
    # Agregamos el nombre a la lista si no es "fin"
    friends.append(friend)

# Mostramos los nombres de los amigos
print("\nYour friends are:")
for friend in friends:
    print(friend)
