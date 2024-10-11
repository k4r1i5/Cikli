SpeletajaVards=input("Ievadi savu vārdu: ")

SpeletajaVards=SpeletajaVards.lower()
#"mainigais.lower() konverte burtus par mazjiem burtiem"

SpeletajaVards=SpeletajaVards.capitalize()
# "mainigais.capitalize()" - pirmo burtu raksta ka lielo burtu

print(SpeletajaVards)

vards1="čība"

burtuSK=len(vards1)
print(burtuSK)
# len - saskaite virknē simbolu skaitu.
minejums=input(f"Uzraksti vārdu pareizi- {vards1[3]}{vards1[0]}{vards1[2]}{vards1[1]}")
# mainigais[burta pozicija] - simbolu virkne sākās ar indeksu - 0.

minejums=minejums.lower()

if minejums==vards1:
    print("Uzminēji vārdu!")
else:
     print("Nuzminēji vārdu!")