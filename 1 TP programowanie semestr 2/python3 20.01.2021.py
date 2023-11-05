zmienna = 1  # Zmienna nie jest wykorzystywana w kodzie, więc można ją usunąć

listX = ["1", "i", "s", "t"]
listY = ["a", "r", "r", "a", "y"]

print("Normal list:", listX)

listX.append("y")  # Dodaj element "y" na koniec listy
print("Appended:", listX)

listX.insert(0, "L")  # Wstaw "L" na początek listy
print("Insert:", listX)

listX.extend(listY)  # Rozszerz listę X o zawartość listy Y
print("Extended:", listX)

listX.sort()  # Posortuj listę X (elementy muszą być porównywalne)
print("Sorted:", listX)

listX.reverse()  # Odwróć listę X
print("Reversed:", listX)

count_y = listX.count("y")  # Zlicz wystąpienia "y" w liście
print("Count:", count_y)