def main():
    niz = unesi_elemente()
    sortiraj_niz(niz)
    ispisi_niz(niz)

def unesi_elemente():
    brojEl = int(input("Koliko elemenata zelite: "))
    niz = []
    for i in range(0, brojEl):
        niz.append(int(input(f"Unesite element {i}: ")))
    
    return niz

def sortiraj_niz(niz):
    for i in range(0, len(niz) - 1, 1):
        for j in range(0, len(niz) - i - 1, 1):
            if(niz[j] > niz[j+1]):
                kanta = niz[j]
                niz[j] = niz[j+1]
                niz[j+1] = kanta

def ispisi_niz(niz):
    print(niz)

if __name__ == '__main__':
    main()
    