##@package generator
# Służy do wygenerowania, zapisu i odczytu danych z pliku.

import numpy.random as random
import numpy as np
from datetime import datetime

global seed
global prawdopodobienstwo_powtorzenia_poprzedniego_odwolania
global replay_odwolan

##Funkcja odtwarzająca menu w konsoli
def menu():
    global prawdopodobienstwo_powtorzenia_poprzedniego_odwolania
    global replay_odwolan
    algorytm = None
    lista_odwolan = []
    print("__MENU__")
    print("1. Wygeneruj dane testowe")
    print("2. Załaduj wygenerowane dane z pliku CSV")
    print("3. Przeprować test na dużym zestawie dancyh")

    opcja = int(input("opcja>"))
    ilosc_ramek = int(input("ilosc ramek>"))
    if opcja == 1:
        ilosc_odwolan = int(input("Ile odwołań wygenerować? >"))
        rozklad_odwolan_str = \
            input("Czy rozkład odwołań ma być jednakowy (0,9), czy częściej mają być generowane ponownie ostatnie odwołania? J/O >")

        rozklad_odwolan = rozkladyOdwolan.OSTATNI_CZESCIEJ if rozklad_odwolan_str == "O" else rozkladyOdwolan.NORMALNY
        try:
            lista_odwolan = generuj_dane(ilosc_odwolan, rozklad_odwolan)
        except Exception as e:
            print("Wystąpił błąd podczas generowania odwołań!", e)
            quit(-1)

    elif opcja == 2:
        plik = input("Podaj ścieżkę do pliku (csv) > ")

        try:
            lista_odwolan = wczytaj_dane(plik)

        except Exception as e:
            print("Wystąpił błąd podczas generowania odwołań!", e)
            quit(-1)

    elif opcja == 3:
        seed = int(input("Podaj seed:"))
        prawdopodobienstwo_powtorzenia_poprzedniego_odwolania = int(input("Podaj prawdopodobienstwo powtarzania sie ostatnich odwolan 0-100 >:"))
        replay_odwolan = \
            int(input("Ile ostatnich odwolan ma być użytych? >:"))
        setSeed(seed)


        return [], [], "test"

    print("__MENU__")
    print("Jakiego algorytmu użyć?")
    print("1. FIFO")
    print("2. LFU")
    opcja = int(input("opcja>"))

    if opcja == 1:
        algorytm = "FIFO"
    elif opcja == 2:
        algorytm = "LFU"

    return lista_odwolan, ilosc_ramek, algorytm


## Ustawia globalny seed na generator
def setSeed(sd):
    global seed
    random.seed(sd)
    seed = sd


class rozkladyOdwolan:
    NORMALNY=0
    OSTATNI_CZESCIEJ=1

##Generator danych.
# Zapisuje on dane automatycznie do pliku do folderu ./data
# Nazwa odpowiada dacie oraz godzinie wykonania programu
def generuj_dane(ilosc_odwolan, rozklad_odwolan=rozkladyOdwolan.NORMALNY, quiet=False, prawdop_powt_odwl=40, ostatnich=5):
    odwolania = []
    if not quiet:
        teraz = datetime.now()
        dt_string = teraz.strftime("%d-%m-%Y_%H-%M-%S")
        export_file = open("data/odwolania_" + dt_string + ".csv", "a+")


    for i in range(ilosc_odwolan):
        # 5% prawdopodobieństwo, że wylosuje ponownie odwołanie to tego samego elementu co w 5 ostatnich odwolaniach.
        if random.randint(0,100) <= prawdop_powt_odwl and rozklad_odwolan == rozkladyOdwolan.OSTATNI_CZESCIEJ and len(odwolania)>2:
            odwolanie = random.choice(odwolania[-ostatnich:len(odwolania)])
        else:
            odwolanie = random.randint(0,9)
        odwolania.append(odwolanie)
        if not quiet:
            export_file.write(f"{odwolanie}\n")
    return odwolania


##Funkcja służąca do czytania danych z pliku
def wczytaj_dane(plik):
    lista_odwolan = []
    import_lines = open(plik, "r").readlines()

    for line in import_lines:
        line = line.replace("\n", "")
        if not line:
            continue
        lista_odwolan.append(int(line))

    return lista_odwolan

