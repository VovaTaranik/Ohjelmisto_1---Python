luvut = []

while True:
    user_input = input("Enter a number or hit Enter to quit: ")
    if user_input == '':
        break
    luvut.append(int(user_input))

luvut.sort(reverse=True)
print("Five greatest numbers:", luvut[:5])