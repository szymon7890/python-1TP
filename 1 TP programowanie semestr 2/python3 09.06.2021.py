# utworzenie funkcji gettingLongestWord oraz podanie parametru array.
def gettingLongestWord(array):
    # utworzneie zmiennej lengths w celu zgromadzenia długości wszystkich wyrazów.
    lengths = []
    # utworznie pętli w celu przeiterownaia zmiennej array w celu zgromadzenia długości poszczególnych elementów tablicy.
    for word in array:
        lengths.append(len(word)) 
    # utworzenie pętli w celu znalezienia oraz zwrócenia najdłuszego słowa listy     
    for word in array:
        if (max(lengths) == len(word)):
            return word
# wywołanie funkcji gettingLongestWord wraz z parametrem jakim jest tablica wyrazów
print(gettingLongestWord(["Krzysiek","Michał","Mikołaj","Igor","Jakub","phpmykrzysiek"]))

# utworzenie funkcji string check oraz podanie parametru text
def stringCheck(text):
    # utworzenie dwóch zmiennych Count w celu zliczenia ilości wystąpień konkretnych liter
    xCount = 0
    oCount = 0
    # utworzenie pętli w celu sprawdzenia ilości występowania liter o i x
    for letter in text:
        if (letter == 'x' or letter == 'X'):
            xCount += 1
        if (letter == 'o' or letter == 'O'):
            oCount += 1
    # sprawdzenie czy ilość obu liter znajdujących się w tekście jest równa oraz zwrócenie wartości logicznej
    if xCount == oCount:
        return True
    else:
        return False
    
# wywołanie funkcji stringCheck oraz podanie parametru.
print(stringCheck('xxXXooOO'))