def wyswietl_parzyste(lista_liczb):
    print("Liczby parzyste:")
    for liczba in lista_liczb:
        if liczba % 2 == 0:
            print(liczba)

liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
wyswietl_parzyste(liczby)