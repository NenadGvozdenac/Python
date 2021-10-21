import docx2txt as do

def main():
    dokument = do.process("text.docx")

    print(dokument)


if __name__ == '__main__':
    main()
    