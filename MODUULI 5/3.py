def onAlkuluku(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

user_input = int(input("Syötä numero: "))
if onAlkuluku(user_input):
    print(user_input, "on alkuluku.")
else:
    print(user_input, "ei ole alkuluku.")