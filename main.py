## @package main
# Plik main

import generator as gen
from zastepowanie_stron import *

## Funkcja main, rozpoczynająca program
def main():
    lista_odwolan, ilosc_ramek, algorytm = gen.menu()
    manadzer = manadzer_odwolan(lista_odwolan, ilosc_ramek, algorytm)
    chybaienia, trafienia  = manadzer.symulacja()

    print(f"Wykonano: {chybaienia} chybień i {trafienia} trafień.")


if __name__=="__main__":
    main()