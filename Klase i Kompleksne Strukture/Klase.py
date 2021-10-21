class Covek():
    def trci(self):
        print("Covek trci!")
        
    def hoda(self):
        print("Covek hoda!")

    def getIme(self):
        return self.ime

    def getGodine(self):
        return self.godine
    
    def __init__(self, godine, ime):
        self.godine = godine
        self.ime = ime

def main():
    covek = Covek(23, "Nenad")
    covek.trci()
    covek.hoda()

    print(covek.getIme())
    print(covek.getGodine())

if __name__ == '__main__':
    main()
    