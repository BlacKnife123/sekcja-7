#TYPY ZAGNIEŻDZONE

imie = "Piotr"
wiek = 20
plec = "Męszczyzna"


imie2 = "Arek"
wiek2 = 25
plec2 = "Męszczyzna"



#lista w liście
listaGosci = [

                ["Piotr",20,"Men"],
                ["Arek",25,"Men"]
]

#krotka w liscie najczesciej stosowane
listaGosci2 = [

                ("Piotr",20,"Men"),
                ("Arek",25,"Men")
    
]

#krotka w krotce
listaGosci3 = (

                ("Piotr",20,"Men"),
                ("Arek",25,"Men")
    
)

#krotka w zbierze
listaGosci4 = {

                ("Piotr",20,"Men"),
                ("Arek",25,"Men")
    
}

listaGosci5 = {

                ("test",20,"Men"),
                ("Ania",25,"Women")

}

for imie,wiek,plec in listaGosci:
    print("Imie: ",imie)
    print("Wiek: ",wiek)
    print("Plec:", plec)
    print("\n")


