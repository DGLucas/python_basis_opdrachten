# Opdracht 2 lists
# Naam student:
# Groep:


rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())
print(rivieren[0].capitalize())
print(rivier_info['rijn'][1].capitalize(),"In de rivier", rivieren[0].capitalize())
print(rivier_info['rijn'][2].capitalize())

#Fout want verkeerdom   print("Antwoord: De rivier", rivier_info['rijn'][1].capitalize(),"stroomt onder andere door", rivieren[0].capitalize())

print("Antwoord: De rivier", rivieren[0].capitalize() ,"stroomt onder andere door", rivier_info['rijn'][1].capitalize())

print("Antwoord: De rivier", rivieren[1].capitalize() ,"stroomt onder andere door", rivier_info['maas'][0].capitalize())
print("Antwoord: De rivier", rivieren[2].capitalize() ,"stroomt onder andere door", rivier_info['nijl'][2].capitalize())

# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

# Hier jouw code.....