# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Vraag de gebruiker om minimaal 5 steden één voor één in te voeren
steden = []
while len(steden) < 5:          #len(steden) gebruikt om te controleren of er al minstens 5 steden zijn ingevoerd
    stad = input(f"Voer stad {len(steden) + 1}: ")      #+1 anders staat er stad 0,1,2,3,4
    steden.append(stad)

# Sorteer de lijst in omgekeerde volgorde, zodat steden die met een 'Z' beginnen vooraan staan
steden.sort(reverse=True, key=lambda stad: stad.lower())

# Print de gesorteerde lijst
print(steden)
