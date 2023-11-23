# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

gasten = ["Lucas", "Paul", "Kees", "Marie", "Hilda"]


# Print de oorspronkelijke lijst
print(gasten)

# Verwijder Marie uit de lijst
gasten.remove("Marie")

# Print de bijgewerkte lijst zonder Marie
print(gasten)

# Voeg George naast Kees toe
kees_index = gasten.index("Kees")
gasten.insert(kees_index + 1, "George")

# Print de bijgewerkte lijst met George naast Kees
print(gasten)
