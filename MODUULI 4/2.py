while True:
    tuumat = float(input("Kirjoita tuumat: "))
    if tuumat < 0:
        break
    cm = tuumat * 2.54
    print("%.2f tuumaa on %.2f cm" % (tuumat, cm))