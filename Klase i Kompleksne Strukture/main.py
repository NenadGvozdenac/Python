def main():
    osobe = {
        "Gvozdenacb" :"Nenad", 
        "Gvozdenace" :"Veljko", 
        "Gvozdenaca" :"Svetlana", 
        "Gvozdenac" :"Marko", 
        "Aleksandar":"Varga",
        "Milivojevic": "Petar"
    }

    for kljuc, osoba in osobe.items():
        print(kljuc + " : " + osoba)

    print("---------")

    for kljuc in osobe.items():
        print(kljuc)
        


if __name__ == '__main__':
    main()
    