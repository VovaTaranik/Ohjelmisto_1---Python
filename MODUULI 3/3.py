sukupuoli = str(input("Mikä sinun sukupuoli on (M/N)?"))
hemo = int(input("Mikä sinun hemoglobiiniarvo on?"))


if (sukupuoli == 'M'):
    if (hemo > 195):
        print("Liian korkea hemoglobiiniarvo sinulla!")
    elif (hemo <= 195 and hemo >= 134):
        print('Sinulla on normaali hemoglobiiniarvo')
    else:
        print("Liian alhainen hemoglobiinitaso!!")
else:
    if (hemo > 175):
        print("Liian korkea hemoglobiiniarvo sinulla!")
    elif (hemo <= 175 and hemo >= 117):
        print(print('Sinulla on normaali hemoglobiiniarvo'))
    else:
        print("Liian alhainen hemoglobiinitaso!!")


