#!/usr/bin/env python3

from poistenci import Poistenci


poistenci = Poistenci()
poistenci.get_nadpis()


pokracovat = True
while pokracovat:
    poistenci.get_moznosti()
    moznost = poistenci.set_moznost()

    if moznost == 1:
        poistenci.pridaj_poistenca()

    elif moznost == 2:
        poistenci.zobraz_poistencov()

    elif moznost == 3:
        poistenci.najdi_poistenca()

    elif moznost == 4:
        print('\nKoniec programu...')
        pokracovat = False
    else:
        pass
