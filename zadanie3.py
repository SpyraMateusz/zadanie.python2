def policz_litery(tekst, litera):
    return tekst.lower().count(litera.lower())

moj_tekst = "Przykładowy Tekst"
dana_litera = 't'
liczba_wystapien = policz_litery(moj_tekst, dana_litera)

print(f"Liczba wystąpień litery '{dana_litera}' w tekście: {liczba_wystapien}")