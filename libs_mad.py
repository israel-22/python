# Solicita al usuario ingresar las palabras necesarias para la historia
print("Please enter the following:")

adjective = input("Adjective: ")
animal = input("Animal: ")
verb1 = input("Verb: ")
exclamation = input("Exclamation: ").capitalize()  # Capitaliza la exclamación
verb2 = input("Verb: ")
verb3 = input("Verb: ")

# Define la historia con las palabras del usuario
story = f"""
The other day, I was really in trouble. It all started when I saw a very
{adjective} {animal} {verb1} down the hallway. "{exclamation}!" I yelled. But all
I could think to do was to {verb2} over and over. Miraculously,
that caused it to stop, but not before it tried to {verb3}
right in front of my family.
"""

# Muestra la historia completa
print("\nYour story is:")
print(story)


