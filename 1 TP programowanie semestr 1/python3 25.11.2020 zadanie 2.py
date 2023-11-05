# Zadanie: Utwórz metodę, która pobierze liczbę oraz zwróci ją w formie binarnej (2 => “10”, 4 => “100”, 5 => “101”, itd.).

# Utworzenie funkcji showBinaryNumber
def showBinaryNumber():
    # Zapisanej do zmiennej userInput liczby podaj przez użytkownika
    userInput = input("Podaj liczbę: ")
    # Wyświetlenie w systemie binarnym sparsowanego ciągu znaków do integer 
    print(bin(int(userInput)))

# Uruchomienie funkcji showBinaryNumber
showBinaryNumber()