def main():
    n=int(input())

    for i in range(n):
        word1=input()
        word2=input()
        dif=""
        for x in range(len(word1)):
            if(word1[x]==word2[x]):
                dif+="."
            else:
                dif+="*"

        print(word1)
        print(word2)
        print(dif)



if __name__ == '__main__':
    main()