# wprowadzenie do zbiorów

"""
     czy:   el. unikalne | kolejność | zmiana konkretnego el. | nowe elementy
listy          NIE           TAK             TAK                   TAK
krotki         NIE           TAK             NIE                   NIE
słowniki       TAK           NIE             TAK                   TAK
zbiory         TAK           NIE             NIE                   TAK

        ZBIORY: BONUS w postaci | & - ^ 
"""

A = {1,2,3,4,5,6}

A.add(7)

B = {2,5,7,9,0,1,4}

print(A)
print(B)
print(A|B)