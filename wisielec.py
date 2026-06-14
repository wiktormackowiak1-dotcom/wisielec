import random

with open("slowa.txt", "r", encoding="utf-8") as plik:
    slowa = []

    for linia in plik:
        linia = linia.strip()
        if linia:
         slowa.append(linia)

slowo = random.choice(slowa)
odkryte = ["_"] * len(slowo)
proby = len(slowo)
uzyte = []

print("=== WISIELEC ===")

while proby > 0 and "_" in odkryte:
    print("\nSłowo:", " ".join(odkryte))
    print("Pozostałe próby:", proby)
    print("Użyte litery:", ", ".join(uzyte))

    litera = input("Podaj literę: ").lower()

    if len(litera) != 1 or not litera.isalpha():
        print("Podaj jedną literę!")
        continue

    if litera in uzyte:
        print("Ta litera była już podana.")
        continue

    uzyte.append(litera)

    if litera in slowo:
        for i in range(len(slowo)):
            if slowo[i] == litera:
                odkryte[i] = litera
        print("Dobrze!")
    else:
        proby -= 1
        print("Źle!")

if "_" not in odkryte:
    print("\nGratulacje! Odgadłeś słowo:", slowo)
else:
    print("\nKoniec gry. Szukane słowo to:", slowo)
