    
#Utwórz funkcje, która po podaniu dowolnej litery alfabetu zwróci 5 następnych liter.
#Przykład (a->b,c,d,e,f |z->a,b,c,d,e).​
#*Dodatkowo uwzględnij małej i dużej litery oraz spraw aby nie można było podać wartości innej niż litera.



# Utworzenie tablicy ze wszystkimi literami alfabetu oraz dodałem litery zapętlające alfabet by działało
lettersArray = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "w", "x", "y", "z", 'a', 'b', 'c', 'd', 'e']
# Utworzenie funkcji nextLetterReturns
def nextLetterReturns(letter):
    # sprawdzenie czy podany znak jest literą
    if letter.isalpha():
        # wykonanie 5 razy pętli for
        for i in range(1, 6):
            # wyświetlenie kolejnych liter oraz obsługa wielkich liter
            print(lettersArray[i + lettersArray.index(letter.lower())])
    else:
        # informacja o błednie podanym znaku
        print('podany znak nie jest literą, spróbuj ponownie')
# Wywołanie funkcji nextLetterReturns
nextLetterReturns('A')