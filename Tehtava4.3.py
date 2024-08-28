luku = int(input("Syötä luku: "))
pienin = suurin = luku
ei_merkkijono = True

while ei_merkkijono:
    syote = input("Syötä luku: ")
    if syote != "":
        uusi_luku = int(syote)
        if uusi_luku > suurin:
            suurin = uusi_luku
        elif uusi_luku < pienin:
            pienin = uusi_luku
    else:
        ei_merkkijono = False

print(f"Pienin luku on {pienin} ja suurin luku on {suurin}.")