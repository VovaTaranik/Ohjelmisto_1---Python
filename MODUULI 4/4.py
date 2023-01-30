import random

luku = random.randint(1, 10)

while True:
    arvaus = int(input("Syötä arvaus (1-10): "))
    if arvaus == luku:
        print("Oikein!")
        break
    elif arvaus > luku:
        print("Liikaa.")
    else:
        print("Liian vähän.")
