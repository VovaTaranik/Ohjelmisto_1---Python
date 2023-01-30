import random

nopat = int(input("Monta noppaa heitetään? "))
noppa_summa = 0

for i in range(nopat):
    noppa_summa += random.randint(1, 6)

print("Sum of all dice:", noppa_summa)