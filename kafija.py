print("Sveicināti")

zetoni=0

while zetoni<15:
    print(f"Ir {zetoni} žetoni")

    met=int(input("Cik žetonus ievietosi? : "))

    zetoni+=met

    zetoni=zetoni-15

print(f"Paņem ☕ kafiju un {zetoni} žetonu atlikums!")
