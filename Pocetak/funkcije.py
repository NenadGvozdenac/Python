def main():
    niz = [1, 3, 5, 7, 2, 10, 13, 16, 20]

    najveciEl = vratiNajveci(niz)

    ispisiNiz(niz)
    ispisiNajveci(najveciEl)

def vratiNajveci(niz):
    max = niz[0]
    for i in range(0, len(niz)):
        if(niz[i] > max):
            max = niz[i]
    return max

def ispisiNiz(niz):
    print(niz)

def ispisiNajveci(max):
    print(max)


if __name__ == '__main__':
    main()