import random

def input_lotto_getallen():
    lotto_getallen = set()
    for i in range(6):
        while True:
            try:
                getal = int(input(f"Voer lotto getal {i + 1} in (tussen 1 en 42): "))
                if 1 <= getal <= 42 and getal not in lotto_getallen:
                    lotto_getallen.add(getal)
                    break
                else:
                    print("Ongeldig getal of getal is al gebruikt. Voer een nieuw getal in.")
            except ValueError:
                print("Ongeldige invoer. Voer een getal tussen 1 en 42 in.")

    return list(lotto_getallen)

def simulate_trekking():
    return random.sample(range(1, 43), 6)  # Gebruik random.sample om unieke getallen te krijgen

def validate_prijzen(ingevoerde_getallen, getrokken_getallen):
    overeenkomende_getallen = set(ingevoerde_getallen) & set(getrokken_getallen)
    aantal_overeenkomsten = len(overeenkomende_getallen)

    if aantal_overeenkomsten == 3:
        print("\nGefeliciteerd! Je hebt 3 juiste cijfers en wint 10 euro.")
    elif aantal_overeenkomsten == 4:
        print("\nGefeliciteerd! Je hebt 4 juiste cijfers en wint 1000 euro.")
    elif aantal_overeenkomsten == 5:
        print("\nGefeliciteerd! Je hebt 5 juiste cijfers en wint 100.000 euro.")
    elif aantal_overeenkomsten == 6:
        print("\nGefeliciteerd! Je hebt 6 juiste cijfers en wint 10.000.000 euro.")
    else:
        print("\nHelaas, geen prijs deze keer. Probeer het opnieuw!")

    print("\nIngevoerde getallen:", sorted(ingevoerde_getallen))
    print("Getrokken getallen:", sorted(getrokken_getallen))

def main():
    ingevoerde_getallen = input_lotto_getallen()
    getrokken_getallen = simulate_trekking()
    validate_prijzen(ingevoerde_getallen, getrokken_getallen)

if __name__ == "__main__":
    main()
