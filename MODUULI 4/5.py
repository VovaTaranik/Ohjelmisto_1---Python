username = "vova"
password = "greis"

attempts = 0


while attempts < 5:
    input_username = input("Syötä käyttäjätunnus: ")
    input_password = input("Syötä salasana: ")
    if input_username == username and input_password == password:
        print("Tervetuloa!")
        break
    else:
        attempts += 1
        print("Väärät tiedot, yritä uudestaan.")

if attempts == 5:
    print("Pääsy kieletty.")
