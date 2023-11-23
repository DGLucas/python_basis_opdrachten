# Opdracht 1 functies
# Naam student:
# Groep:


def volledige_naam(lijst_met_namen):
    for naam in lijst_met_namen:
        # Bouw de volledige naam op basis van de dictionary-elementen
        volledige_naam = f"{naam['voornaam']} {naam['tussenvoegsel']} {naam['achternaam']}".strip()
        
        # Toon de volledige naam op het scherm
        print(volledige_naam)

# Test de functie
namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

volledige_naam(namen)
