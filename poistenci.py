CHYBA = "Neplatná voľba - vyberte z možností 1 až 4..."
TABULATOR = 20
POKRACUJTE = "\nPokračujte klávesou ENTER..."
HLAVICKA_TABULKY = f'\nMeno: \t Priezvisko: \t Vek: \t Telefónne Číslo:'


class Poistenci:

    def __init__(self):
        self.zoznam_poistencov = []

    # def __str__(self):
        # return f"{self.meno} \t {self.priezvisko} \t {self.vek} \t {self.tel_cislo}".expandtabs(TABULATOR)

    @staticmethod
    def get_nadpis():
        print(30 * u"\u2014" + "\nEvidencia poistencov\n" + 30 * u"\u2014")

    @staticmethod
    def get_moznosti():
        print("\nVyberte z možností:\n" +
              "1 - Pridať nového poistenca\n" +
              "2 - Zobraziť všetkých poistencov\n" +
              "3 - Vyhľadať poistenca\n" +
              "4 - Koniec\n")

    @staticmethod
    def set_moznost():
        while True:
            try:
                cislo = int(input("Zadajte možnosť: "))
                if cislo not in range(1, 5):
                    print(CHYBA)
            except ValueError:
                print(CHYBA)
            else:
                return cislo

    def pridaj_poistenca(self):
        meno = input("\nZadajte meno poistenca: \n")
        priezvisko = input("Zadajte priezvisko: \n")
        vek = input("Zadajte vek: \n")
        tel_cislo = input("Zadejte telefónne číslo: \n")
        self.zoznam_poistencov.append((meno, priezvisko, vek, tel_cislo))
        input("\nÚdaje boli uložené. Pokračujte klávesou ENTER...")

    def zobraz_poistencov(self):
        print(HLAVICKA_TABULKY.expandtabs(TABULATOR))
        for poistenec in self.zoznam_poistencov:
            print(f'{poistenec[0]} \t {poistenec[1]} \t {poistenec[2]} \t {poistenec[3]}'.expandtabs(TABULATOR))
        input(POKRACUJTE)

    def najdi_poistenca(self):
        hladane_meno = input("Zadaj hľadané meno: ")
        hladane_priezvisko = input("Zadaj priezvisko: ")
        nasiel_sa = False
        for poistenec in self.zoznam_poistencov:
            if hladane_meno == poistenec[0] and hladane_priezvisko == poistenec[1]:
                self.get_poistenec(poistenec=poistenec)
                nasiel_sa = True
        if not nasiel_sa:
            print(f'\n{hladane_meno} {hladane_priezvisko} sa v zozname poistencov nenachádza...')
            input(POKRACUJTE)

    @staticmethod
    def get_poistenec(poistenec):
        print('\nHľadaný poistenec v zozname:')
        print(HLAVICKA_TABULKY.expandtabs(TABULATOR))
        print(f'{poistenec[0]} \t {poistenec[1]} \t {poistenec[2]} \t {poistenec[3]}'.expandtabs(TABULATOR))
        input(POKRACUJTE)
