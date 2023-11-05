#komentarz Wprowadzenie do języka Python
#typ zmienna w pythonie definiowany jest na podstawie wartosci jka ta zmienna posiada
#NAZWY ZMIENNYCH NIE POWINNY ZAWIERAĆ SPACJI ORAZ NAZW ZASTRZEŻONYCH
#typ string -tekst
zmienna1="text"
#typ int -liczba całkowita
zmienna2=-1
#typ bool -zmienna logiczna
zmienna3=True
#typ float -zmienna zmiennoprzecinkowa
zmienna4=1.25
#typ array -zmienna listy
zmienna5=[1,"text",3.5,False]

#Funckja wbudowana print
print("Funkcje przed konwersją na typ int",zmienna2,zmienna3,zmienna4)
print("Funkcje po konwersją na typ int",zmienna2,int(zmienna3),int(zmienna4))
print(zmienna5,end="-koniec lini-\n")
print("t","e","x","t",sep="[spam]")
print("She's")
print('"She is"')

#pętle
print("Petla for")
for x in range(5):
    print(x)

print("Petla while")
licznik = 0
while licznik < 5:
    print (licznik)
    licznik += 1 