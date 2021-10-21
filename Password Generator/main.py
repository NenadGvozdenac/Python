import random as rand

karakteri = "1234567890qwertyuiopasdfghjklzxcvbnm"

def main():
    password = ""
    for i in range(0, 15):
        broj = rand.randint(0, len(karakteri) - 1)
        password += karakteri[broj]
    
    print(f"Nova sifra je: {password}")

if __name__ == '__main__':
    main()
    