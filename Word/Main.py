import docx 

def main():
    dokument = docx.Document("text.docx")

    for i in dokument.paragraphs: 
        print(i)


if __name__ == '__main__':
    main()
    