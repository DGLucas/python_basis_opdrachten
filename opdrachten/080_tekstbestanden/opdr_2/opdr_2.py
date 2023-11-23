# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

#import random
#prompt = "Raad mijn geheime getal \n"
#geheim_getal = random.randint(1, 100)

# De rest moet jij doen.....

import random
prompt = "Raad mijn geheime getal tussen 1 en 100\n"
geheim_getal = random.randint(1, 100)

aantal_pogingen = 0

print(prompt)

while True:
    gebruiker_invoer = int(input())
    aantal_pogingen += 1

    if gebruiker_invoer < geheim_getal:
        print("hoger")
    elif gebruiker_invoer > geheim_getal:
        print("lager")
    else:
        print(f"Je hebt het getal geraden, het is {geheim_getal}!")
        print(f"Je hebt het in {aantal_pogingen} keer geraden.")
        break
