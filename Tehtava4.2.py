tuumat = float(input("Anna tuumat:"))
while tuumat >= 0:
    print(f"{tuumat * 2.54:.2f} cm")
    print()
    tuumat = float(input("Anna tuumat uudestaan: "))
    if tuumat < 0:
        print("Negatiivinen luku")
        break