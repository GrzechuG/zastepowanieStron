## @package main
# Plik main

import generator as gen
from zastepowanie_stron import *
import copy
from datetime import datetime


## Funkcja main, rozpoczynająca program
def main():
    lista_odwolan, ilosc_ramek, algorytm = gen.menu()
    if algorytm == "test":
        test_na_duzym_zestawie_dancyh()
        quit()
    manadzer = manadzer_odwolan(lista_odwolan, ilosc_ramek, algorytm)
    chybaienia, trafienia  = manadzer.symulacja()

    print(f"Wykonano: {chybaienia} chybień i {trafienia} trafień.")

##Przeprowadza automatycznie porównanie obu algorytmów i generuje raport.
def test_na_duzym_zestawie_dancyh():
    teraz = datetime.now()
    dt_string = teraz.strftime("%d-%m-%Y_%H-%M-%S")
    nazwa_pliku = "raports/raport_" + dt_string + ".csv"
    sprawozdanie = open(nazwa_pliku, "a+")
    #szerokosc ramki stała ~ 4
    # ilosc zastąpnień - stała 100

    sprawozdanie.write("chybienia(FIFO, NORMALNY); trafienia(FIFO, NORMALNY); chybienia(LFU, NORMALNY); trafienia(LFU, NORMALNY);"
                       f"chybienia(FIFO, OSTATNIE_CZESCIEJ); trafienia(FIFO, OSTATNIE_CZESCIEJ); chybienia(LFU, OSTATNIE_CZESCIEJ); trafienia(LFU, OSTATNIE_CZESCIEJ); seed={gen.seed} \n")
    ilosc_ramek = 4
    for i in range(100):
        record = []
        lista_odwolan = gen.generuj_dane(
            100,
            rozklad_odwolan=gen.rozkladyOdwolan.NORMALNY,
            quiet=True,
            prawdop_powt_odwl=0)

        manadzerFIFO = manadzer_odwolan(copy.deepcopy(lista_odwolan), ilosc_ramek, "FIFO")
        manadzerLFU = manadzer_odwolan(copy.deepcopy(lista_odwolan), ilosc_ramek, "LFU")
        chybaieniaFIFO, trafieniaFIFO = manadzerFIFO.symulacja()
        chybaieniaLFU, trafieniaLFU = manadzerLFU.symulacja()
        record+=[chybaieniaFIFO, trafieniaFIFO, chybaieniaLFU, trafieniaLFU]

        lista_odwolan = gen.generuj_dane(
            100,
            rozklad_odwolan=gen.rozkladyOdwolan.OSTATNI_CZESCIEJ,
            quiet=True,
            prawdop_powt_odwl=gen.prawdopodobienstwo_powtorzenia_poprzedniego_odwolania,
            ostatnich=gen.replay_odwolan
        )

        manadzerFIFO = manadzer_odwolan(copy.deepcopy(lista_odwolan), ilosc_ramek, "FIFO")
        manadzerLFU = manadzer_odwolan(copy.deepcopy(lista_odwolan), ilosc_ramek, "LFU")
        chybaieniaFIFO, trafieniaFIFO = manadzerFIFO.symulacja()
        chybaieniaLFU, trafieniaLFU = manadzerLFU.symulacja()
        record += [chybaieniaFIFO, trafieniaFIFO, chybaieniaLFU, trafieniaLFU]

        record_str = [str(rec) for rec in record]
        sprawozdanie.write(";".join(record_str)+"\n")
    print("Wygenerowano raport: ", nazwa_pliku)


if __name__=="__main__":
    main()