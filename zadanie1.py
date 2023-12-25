def oblicz_srednia(oceny):
    if not oceny:
        return 0  

    suma_ocen = sum(oceny)
    srednia = suma_ocen / len(oceny)
    return srednia

oceny_studenta = [4.5, 3.0, 5.0, 4.0, 3.5]
srednia_ocen = oblicz_srednia(oceny_studenta)
print(f"Średnia ocen: {srednia_ocen}")