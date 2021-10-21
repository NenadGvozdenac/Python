def main():
    stringNiz = []

    unesi_elemente(stringNiz)
    ispisi_elemente(stringNiz)

def unesi_elemente(strNiz):
    brEl = int(input("Unesite broj elemenata: "))

    for i in range(0, brEl):
        strNiz.append(str(input(f"Unesite string element {i}: ")))

def ispisi_elemente(strNiz):
    print(strNiz)


if __name__ == '__main__':
    main()