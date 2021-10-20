velicinaNiza = 15

lista = []

for i in range(0, velicinaNiza):
    lista.append(int(input(f"Unesite {str(i)}: ")))


max = lista[0]

for i in range(0, len(lista)):
    if(lista[i] > max):
        max = lista[i]

print(f"Najveci element je: {str(max)}")