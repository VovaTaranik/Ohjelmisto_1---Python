kaupungit = []

for i in range(5):
    kaupunki = input(f"Enter the name of city {i + 1}: ")
    kaupungit.append(kaupunki)

print("\nKaupungit:")
for kaupunki in kaupungit:
    print(kaupunki)