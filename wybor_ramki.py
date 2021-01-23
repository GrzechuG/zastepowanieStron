## @package wybor_ramki
# Plik zawiera klasę algorytmy

##Klasa algorytmy zawiera funkcje wybierania odpowiedniej ramki
class algorytmy:

    ##Konstruktor
    def __init__(self):
        self.ostatni = -1

    ##Algorytm First In First Out
    def FIFO(self, ilosc_ramek):
        self.ostatni = (self.ostatni+1)%ilosc_ramek
        return self.ostatni

    ##Algorytm Least Frequently Used.
    #Jako argumenty należy podać listę odwołań do danego momentu oraz pamięć ramek.
    def LFU(self, lista_odwolan, pamięć):


        if pamięć:
            najrzadziej_używany = 0
            najmniejsza_ilosc_odwolan = lista_odwolan.count(pamięć[0])
            for i in range(len(pamięć)):
                ramka = pamięć[i]

                ilosc_odwolan = lista_odwolan.count(ramka)

                if ilosc_odwolan < najmniejsza_ilosc_odwolan:
                    najmniejsza_ilosc_odwolan = ilosc_odwolan
                    najrzadziej_używany = i

            return najrzadziej_używany

        return None


