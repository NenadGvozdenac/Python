import random as rand

def main():
    najmanjiEl = int(input("Unesite najmanji element: "))
    najveciEl = int(input("Unesite najveci element: "))

    niz = []

    for i in range(0, 10):
        niz.append(rand.randint(najmanjiEl, najveciEl))

    print(niz)


if __name__ == '__main__':
    main()
    