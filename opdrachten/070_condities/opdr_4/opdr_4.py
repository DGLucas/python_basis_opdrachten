# Opdracht 4 condities
# Naam student:
# Groep:



#toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00) , ("ansjovis", 2.50)]
#beschikbare_toppings = ...

#keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings} \n")

# Hier de rest van jouw code...

# Definieer de beschikbare toppings
toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00), ("ansjovis", 2.50)]

# Bouw een lijst op met alleen de namen van de toppings
beschikbare_toppings = [topping[0] for topping in toppings]     #topping[0]: Dit verwijst naar het eerste element (index 0) van elk topping-element. In de lijst toppings zijn de toppings tuples, en het eerste element van elke tuple is de naam van de topping.

# Vraag de gebruiker om een keuze uit de beschikbare toppings
keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings}\n")

# Controleer of de keuze in de lijst van beschikbare toppings zit
if keuze in beschikbare_toppings:
    # Zoek de prijs van de gekozen topping
    prijs = [topping[1] for topping in toppings if topping[0] == keuze][0]
    
    # Geef de keuze en prijs weer
    print(f"U heeft {keuze} besteld. Dat kost {prijs}")
else:
    print("Uw keuze zit niet in ons assortiment")
