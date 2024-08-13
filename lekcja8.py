"""
Napisz program, który pozwoli użytkownikowi:
1) Dodawać nowe definicje
2) Szukać istniejącej definicji
3) Usuwać wybrane przez niego definicje
"""

definicje ={}

while (True):

    print("Cześć jestem twoim prywatnym słownikiem z definicjami")
    print("1) Dodać nowe definicje")
    print("2) Szukać istniejącej definicji")
    print("3) Usuwać wybrane przez niego definicje")
    print("4) Zakończ program")

    wybor = input("Wybierz co chcesz zrobić: ")

    if wybor == "1":
        klucz = input("Podaj słowo do zdefiniowania: ")
        definicja = input("Podaj definicje: ")
        definicje[klucz] = definicja
        print("Definicja dodana pomyślnie")

    elif wybor == "2":
        klucz = input("Czego szukasz: ")
        if klucz in definicje:
            print(definicje[klucz])
        else:
            print("Nie znaleziono definicji słowa", klucz)
    elif wybor == "3":
        klucz = input("Co chcesz usunąć: ")
        if klucz in definicje:
            del(definicje[klucz])
            print("Usunięto definicje ", klucz)
        else:
            print("Nie znaleziono definicji słowa", klucz)
    elif wybor == "4":
        print("no to pa")
        break
    else:
        print("Podałes cos z poza zakresu")
