name = "aDa lovElace"
print(name.title())
print(name.upper())
print(name.lower())

print("====================")

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
message = ("Hello, " + full_name.title() + "!")
print(message)

print("====================")

# Wyrazenia regularne tab i nowa linia

print("Python")
print("\t Python")

print("")

print("Languages:\nPython\nC\nJavaScript")

print("")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

print("")

print("====================")

# Usuwanie bialych znakow

favourite_language = ' python '
print("|" + favourite_language + "|")
print("|" + favourite_language.rstrip() + "|")
print("|" + favourite_language.lstrip() + "|")
print("|" + favourite_language.strip() + "|")
