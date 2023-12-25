def wyswietl_dzielniki(liczba):
    print(f"Dzielniki liczby {liczba}:")
    for i in range(1, liczba + 1):
        if liczba % i == 0:
            print(i)

moja_liczba = 12
wyswietl_dzielniki(moja_liczba)