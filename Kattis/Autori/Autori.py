

def main():
    word=input()
    out=""
    out+=word[0]
    for x in range(len(word)):
        if(word[x]=="-"):
            out+=word[x+1]

    print(out)




if __name__ == '__main__':
    main()