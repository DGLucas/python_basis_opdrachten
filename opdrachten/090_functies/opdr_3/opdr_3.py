# Opdracht 1 functies
# Naam student:
# Groep:


import math

def kubus_vol(m):
    # Bereken het volume van de kubus met de formule: volume = zijde^3
    volume = m ** 3
    return volume

def bol_vol(r):
    # Bereken het volume van de bol met de formule: volume = (4/3) * pi * straal^3
    volume = (4/3) * math.pi * (r ** 3)
    return volume

# Test de functies
zijde = 5
radius = 4

print(f"De inhoud van deze kubus is: {kubus_vol(zijde)}")
print(f"De inhoud van deze bol is: {bol_vol(radius)}")
