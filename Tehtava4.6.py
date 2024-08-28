import random

pisteidenmaara = int(input("Anna pisteiden määrä: "))
toisto = 0
pisteet_ympyrassa = 0

while toisto < pisteidenmaara:
    piste_x = random.uniform(-1,1)
    piste_y = random.uniform(-1,1)
    toisto = toisto + 1
    if piste_x**2+piste_y**2 < 1:
        pisteet_ympyrassa = pisteet_ympyrassa + 1

print(4*pisteet_ympyrassa/pisteidenmaara)