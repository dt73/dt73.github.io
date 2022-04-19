from random import randint
z=1
while z==1:
    los = randint(1,100)
    odp = int(input("Podaj liczbę od 1 do 100!: "))
    i=1
    while odp != los:
        if odp>los:
            print("Za duża!")
        else:
            print("Za mała!")
        i+=1
        odp = int(input("Podaj liczbę od 1 do 100!: "))
    print ("Zgadłeś za", i, "razem")
    z = int(input("Grasz dalej? Tak-1/Nie-dowolna liczba: "))
print("Koniec gry!")
