def main():
    lista = []

    brEl = int(input("Unesite broj elemenata: "))

    for i in range(0, brEl):
        unos = input(f"Unesite element {i}: ")
        try:
            lista.append(int(unos))
        except: 
            print("Pogresan unos.")
    
    lista.sort()

    print(lista)

if __name__ == '__main__':
    main()
