O_tunnus = "python"
O_salasana = "rules"
yritykset = 1

A_tunnus = input("Anna käyttäjätunnus: ")
A_salasana = input("Anna salasana: ")

while yritykset < 5:
    if A_tunnus != O_tunnus or A_salasana != O_salasana:
        print("Väärä käyttäjätunnus ja/tai salasana.")
        print()
        A_tunnus = input("Anna käyttäjätunnus: ")
        A_salasana = input("Anna salasana: ")
        yritykset = yritykset + 1
    elif A_tunnus == O_tunnus and A_salasana == O_salasana:
        print()
        print("Tervetuloa!")
        break
else:
    print()
    print("Pääsy evätty.")