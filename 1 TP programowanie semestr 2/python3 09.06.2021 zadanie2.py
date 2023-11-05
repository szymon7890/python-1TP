#Zadanie: Utwórz metodę, która pobierze liczbę i wypisze każdy znak w osobnej
#linii zaczynając od ostatniej cyfry (np. dla liczby 123 będą to trzy
#linie z 3, 2 i 1).

# Utworzenie funkcji showReverseWord
def showReverseWord():
    # Zapisanie do zmiennej userInput liczby pobranej od użytkownika
    userInput = input("Podaj liczbę: ")
    # zapisanej do zmiennej userInputReverse odwróconego ciągu znaków
    userInputReverse = userInput[::-1]
    # Utworzenie pętli for w celu wyświetlenia poszczególnych znaków od nowej linii
    for letter in userInputReverse:
        print(letter)

# Uruchomienie funkcji showReverseWord
showReverseWord()