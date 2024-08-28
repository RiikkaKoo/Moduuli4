import random

luku = random.randint(1,10)
print(luku)
arvaus = int(input("Arvaa luku väliltä 1-10: "))
print()
wrong_guess = True

while wrong_guess:
    if arvaus > luku:
        print("Liian suuri arvaus.")
        arvaus = int(input("Arvaa uudestaan: "))
    elif arvaus < luku:
        print("Liian pieni arvaus.")
        arvaus = int(input("Arvaa uudestaan: "))
    elif arvaus == luku:
        print("Oikein!")
        wrong_guess = False