# Zapisanie 10 warzyw w tablicy do zmiennej vegeTable
vegeTable = ['Cebula', 'Pomidor', 'Ziemniaki', 'Kalafior', 'Szczypiorek', 'Por', 'Czosnek', 'Sałata', 'Ogórek', 'Chrzan']

# Ustawienie początkowej wartości licznika
numbers = 1

# Pętla, która przeiteruje tablicę warzyw
for vege in vegeTable:
    # Wyświetlenie numeru i nazwy warzywa
    print(str(numbers) + '-' + vege)
    
    # Zwiększenie licznika o 1
    numbers += 1