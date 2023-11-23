# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

x_values = range(1, 10)
y_values = [4 * x + 7 for x in x_values]

for x, y in zip(x_values, y_values):
    print(f"x = {x}, y = {y}")
