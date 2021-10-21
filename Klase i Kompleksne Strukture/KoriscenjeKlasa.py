class Covek():
    def __init__(self, ime, prezime, godine):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine

    def getIme(self):
        return self.ime

    def getPrezime(self):
        return self.prezime

    def getGodine(self):
        return self.godine

    def ispisiSve(self):
        print(self.ime + ", " + self.prezime + " - " + str(self.godine))


def main():
    covek = Covek("Nenad", "Gvozdenac", 19)

    print(covek.getIme())
    print(covek.getPrezime())
    print(covek.getGodine())

    covek.ispisiSve()

if __name__ == '__main__':
    main()
    