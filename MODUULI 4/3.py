luvut = []

while True:
    luku = input("Syötä luku tai paina entteriä lopettakseen: ")
    if luku == "":
        break
    luvut.append(int(luku))

if luvut:
    print("Pienin luku:", min(luvut))
    print("Suurin luku:", max(luvut))
else:
    print("Luvut ei syötetty.")