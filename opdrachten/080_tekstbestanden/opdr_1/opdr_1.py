# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier

# Stel de vragen aan de gebruiker
antwoord1 = input("Wat vind je van de huidige regering? ")
antwoord2 = input("Wat vind je van de Python-lessen tot nu toe? ")
antwoord3 = input("Wat vind jij de mooiste stad van Nederland? ")

# Maak een tekstbestand aan of open het bestaande bestand om de resultaten op te slaan
with open("enquete_resultaten.txt", "a") as file:
    # Schrijf de antwoorden naar het tekstbestand
    file.write(f"\nAntwoord 1: {antwoord1}\n")
    file.write(f"Antwoord 2: {antwoord2}\n")
    file.write(f"Antwoord 3: {antwoord3}\n")

print("Bedankt voor het invullen van de enquête. De resultaten zijn opgeslagen.")
