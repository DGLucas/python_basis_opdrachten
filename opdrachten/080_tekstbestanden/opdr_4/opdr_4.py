# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


# Party enquete

vragen = ["Wat is je voornaam", "Wat is je achternaam", "Wat neem je mee aan drank", "Wat neem je mee om te eten"]
antwoorden = {}
teller = 1
for vraag in vragen:
    ant = input(str(teller) + " " + vraag +"? ")
    #find last word of vraag
    item = vraag.split()[-1]
    antwoorden[item] = ant
    teller+=1
#write textfile
fo = open('boodschappen.txt', 'at')
for key, value in antwoorden.items():
    fo.write(key + ": "+ value + "\n")
fo.write("\n\n")
fo.close()
print("Bedankt voor het invullen! \n\nSee you at the party.")