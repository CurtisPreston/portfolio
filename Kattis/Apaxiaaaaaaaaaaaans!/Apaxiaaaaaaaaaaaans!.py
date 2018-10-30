#https://open.kattis.com/problems/apaxiaaans


def main():
    text=input()
    out=""
    last=''

    while(len(text)>0):
        if(not(text[0]==last)):
            out+=text[0]
            last=text[0]
            text=text[1:len(text)]

        else:
            last=text[0]
            text = text[1:len(text)]

    print(out)






if __name__ == '__main__':
    main()