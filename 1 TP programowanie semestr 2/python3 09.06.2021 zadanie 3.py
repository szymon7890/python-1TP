# Definicja funkcji wiadomosc
def wiadomosc():
    print("Cześć")  # Ciało funkcji

# Wywołanie funkcji wiadomosc
wiadomosc()

# Definicja funkcji czesc z jednym parametrem imie
def czesc(imie):
    print("Cześć,", imie)  # Ciało funkcji

imie = input("Podaj swoje imię: ")

# Wywołanie funkcji czesc z przekazaniem zmiennej imie jako argumentu
czesc(imie)