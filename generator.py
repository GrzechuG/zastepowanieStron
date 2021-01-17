##@package generator
# Służy do wygenerowania, zapisu i odczytu danych z pliku.

import numpy.random as random
import numpy as np
from datetime import datetime

##Funkcja odtwarzająca menu w konsoli
def menu():
    algorytm = None
    lista_odwolan = []
    print("__MENU__")
    print("1. Wygeneruj dane testowe")
    print("2. Załaduj wygenerowane dane z pliku CSV")

    opcja = int(input("opcja>"))
    ilosc_ramek = int(input("ilosc ramek>"))
    if opcja == 1:

        ilosc_odwolan = int(input("Ile odwołań wygenerować? >"))

        try:
            lista_odwolan = generuj_dane(ilosc_odwolan)
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


##Generator danych.
# Zapisuje on dane automatycznie do pliku do folderu ./data
# Nazwa odpowiada dacie oraz godzinie wykonania programu
def generuj_dane(ilosc_odwolan):
    odwolania = []
    teraz = datetime.now()
    dt_string = teraz.strftime("%d-%m-%Y_%H:%M:%S")
    export_file = open("data/odwolania_" + dt_string + ".csv", "a+")
    for i in range(ilosc_odwolan):
        odwolanie = random.randint(0,9)
        odwolania.append(odwolanie)
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

