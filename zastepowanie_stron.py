## @package zastepowanie_stron
#  Plik zawierający klasę manadzer odwołań

from wybor_ramki import algorytmy as alg
from text_formatting import color

##Klasa manadzer_odwolan służy do przeprowadzenia symulacji algorytmów zastępowania stron
class manadzer_odwolan:

    ##konstruktor klasy
    def __init__(self, lista_odwolan, ilosc_ramek, algorytm):
        self.lista_odwolan = lista_odwolan
        self.ilosc_ramek = ilosc_ramek
        self.pamięć = [None for i in range(ilosc_ramek)]
        self.algorytm = algorytm
        # self.licznik_odwolan = dict()
        self.algorytmy = alg()
        self.historia = []

        self.chybienia = 0
        self.trafienia = 0

    ##Funkcja służąca do wywołania algorytmu odpowiadającego podanemu w konstruktorze
    def wybierz_ramke(self, moment):
        if self.algorytm == "FIFO":
            return self.algorytmy.FIFO(self.ilosc_ramek)
        elif self.algorytm == "LFU":
            return self.algorytmy.LFU(self.lista_odwolan[0:moment], self.pamięć)
        else:
            print("Algorytm ", self.algorytm, "nie jest wspierany!")
            quit(-1)

    # def aktualizuj_licznik_odwolan(self, odwolanie):
    #     if not odwolanie in self.licznik_odwolan:
    #         self.licznik_odwolan[odwolanie] = 1
    #     else:
    #         self.licznik_odwolan[odwolanie] += 1

    ##Funckja, która podmienia odpowiednią ramkę w pamięci
    def dodaj_do_pamięci(self, ramka, odwolanie):
        self.pamięć[ramka] = odwolanie

    ##Funckja służąca do wypisania wykonanej symulacji na ekran
    def rozpisz(self):
        for i in range(self.ilosc_ramek + 2):
            for hist in self.historia:
                if i == 0:
                    print(hist[0], end=" ")
                if i == 1:
                    print("--", end="")

                if i > 1:
                    toPrint = hist[1][i - 2]
                    if toPrint == None:
                        toPrint = " "

                    if toPrint == hist[0]:
                        toPrint = color.GREEN + str(toPrint) + color.END

                    print(toPrint, end=" ")
            print()

    ##Funckja która dokonuje symulacji
    def symulacja(self):

        for j in range(len(self.lista_odwolan)):
            odwolanie = self.lista_odwolan[j]
            # self.aktualizuj_licznik_odwolan(odwolanie)

            if not odwolanie in self.pamięć:

                if None in self.pamięć:
                    for i in range(self.ilosc_ramek):
                        if self.pamięć[i] is None:
                            self.dodaj_do_pamięci(i, odwolanie)

                            break
                else:
                    self.chybienia += 1
                    ramka = self.wybierz_ramke(j)
                    self.dodaj_do_pamięci(ramka, odwolanie)


            else:

                self.trafienia += 1

            self.historia.append((odwolanie, self.pamięć[:]))

        self.rozpisz()

        return self.chybienia, self.trafienia
