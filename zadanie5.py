import math
def oblicz_pierwiastek_kwadratowy(liczba):
    if liczba < 0:
        raise ValueError("Nie można obliczyć pierwiastka ze względu na liczbę ujemną.")
    else:
        return math.sqrt(liczba)

try:
    liczba_uzytkownika = int(input("Podaj liczbę całkowitą: "))

    wynik = oblicz_pierwiastek_kwadratowy(liczba_uzytkownika)
    print(f"Pierwiastek kwadratowy z {liczba_uzytkownika} to: {wynik}")
except ValueError as e:
    print(e)
except Exception as e:
    print(f"Wystąpił błąd: {e}")