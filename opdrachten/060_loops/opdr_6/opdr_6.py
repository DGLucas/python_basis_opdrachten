# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

# De oorspronkelijke lijst met pizza's
pizza_lijst = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

# Sorteer de lijst op alfabetische volgorde
pizza_lijst.sort()
print(pizza_lijst)

# Voeg naar eigen smaak nog een pizza toe
pizza_lijst.append('Salami')
print(pizza_lijst)

# Verwijder de pizza die je het minst lekker vindt (bijv. olivio)
pizza_lijst.remove('olivio')
print(pizza_lijst)

# Print de eerste 3 pizza's uit de lijst
eerste_drie_pizza = pizza_lijst[:3]
print(eerste_drie_pizza)

# Print alleen de middelste pizza uit de lijst
middelste_pizza = pizza_lijst[len(pizza_lijst) // 2]
print([middelste_pizza])

# Print de laatste 3 pizza's uit de lijst
laatste_drie_pizza = pizza_lijst[-3:]
print(laatste_drie_pizza)
