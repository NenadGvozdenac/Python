import pandas as pd

def main():
    dokument = pd.read_excel("nesto.xlsx")

    # for i in dokument.columns:
    #     print(i)

    for i, j in dokument.iterrows():
        print(str(j))



if __name__ == '__main__':
    main()
    