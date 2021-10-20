intbroj = 10

print(str(intbroj * 3) + f" je jednako {str(intbroj)} * 3")
print(str(intbroj ** 3) + f" je jednako {str(intbroj)} ** 3")
print(str(intbroj / 3) + f" je jednako {str(intbroj)} / 3")
print(str(intbroj // 3) + f" je jednako {str(intbroj)} // 3")

print()
floatbroj = 10.60

print(str(round(floatbroj)) + " je zaokruzivanje broja " + str(floatbroj))

negativanbroj = -5

print(str(abs(negativanbroj)) + f" je apsolutno od broja {str(negativanbroj)}")

import math

broj2 = 3.3
broj3 = 3.7

print(str(math.ceil(broj2)) + f" je ceiling od broja {str(broj2)}")
print(str(math.floor(broj3)) + f" je ceiling od broja {str(broj3)}")