# Opdracht 1 lists
# Naam student:
# Groep:

# Maak een lijst aan om de dictionaries op te slaan
mylist = []

# Definieer vier dictionaries met gegevens van personen
dict_1 = { "id": 1, "voornaam": "John", "achternaam": "Doe" }
dict_2 = { "id": 2, "voornaam": "Jane", "achternaam": "Smith" }
dict_3 = { "id": 3, "voornaam": "Bob", "achternaam": "Johnson" }
dict_4 = { "id": 4, "voornaam": "Alice", "achternaam": "Brown" }

# Voeg de dictionaries toe aan de lijst
mylist.append(dict_1)
mylist.append(dict_2)
mylist.append(dict_3)
mylist.append(dict_4)

# Druk de volledige naam van de tweede persoon af
print(mylist[1]["voornaam"], mylist[1]["achternaam"])

#append-methode om een element aan een lijst toe te voegen