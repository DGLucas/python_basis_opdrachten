# Opdracht 3 condities
# Naam student:
# Groep:




#normale_toegangsprijs = 12.50
#kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
#leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Hier komt je code...

normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Vraag de leeftijd van de bezoeker
leeftijd_input = int(input("Geef uw leeftijd in aantal jaar: "))

# Bepaal de leeftijdsgroep
groep = None        #Initialiseer de variabele groep met None, wat betekent dat we aanvankelijk geen leeftijdsgroep hebben gevonden.
for key, value in leeftijd.items():     # Loop door alle items (sleutel-waardeparen) in de dictionary leeftijd.
    if value[0] <= leeftijd_input <= value[1]: # Controleer of de ingevoerde leeftijd binnen 0-150 past
        groep = key     #Als leeftijd klopt
        break #Stop de loop zodra een overeenkomst is gevonden

# Bereken de korting
korting_percentage = kortings_percentages[groep]
korting_bedrag = normale_toegangsprijs * (korting_percentage / 100)

# Bereken de te betalen prijs
te_betalen_prijs = normale_toegangsprijs - korting_bedrag

# Geef de output weer
print(f"U behoort tot de groep {groep}")
print(f"U krijgt {korting_percentage}% korting")
print(f"U betaalt daarom {te_betalen_prijs:.2f}")
