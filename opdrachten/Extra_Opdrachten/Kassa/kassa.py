def main():
    # Vraag om 6 bedragen
    bedragen = []
    for i in range(3):
        while True:
            try:
                bedrag = float(input(f"Voer bedrag {i + 1} in: "))
                if bedrag <= 0:
                    print("Bedrag moet groter zijn dan 0. Probeer opnieuw.")
                else:
                    bedragen.append(bedrag)
                    break
            except ValueError:
                print("Ongeldige invoer. Voer een geldig bedrag in.")

    # Bereken de som van alle bedragen
    totaal_bedrag = sum(bedragen)
    print(f"\nTotale bedrag: {totaal_bedrag:.2f} euro\n")

    # Vraag om het betaalbedrag
    betaalbedrag = 0
    while betaalbedrag < totaal_bedrag:
        try:
            betaalbedrag += float(input("Met hoeveel betaalt u: "))
            if betaalbedrag < totaal_bedrag:
                print(f"Er blijft nog over: {totaal_bedrag - betaalbedrag:.2f} euro")
        except ValueError:
            print("Dit is geen geldige waarde.")

    # Bereken wisselgeld of bedrag dat nog betaald moet worden
    verschil = betaalbedrag - totaal_bedrag

    if verschil > 0:
        print(f"\nU krijgt terug: {verschil:.2f} euro")
    else:
        print("\nBedankt voor het zaken doen.")

if __name__ == "__main__":
    main()
