def main():
    n=int(input())
    for x in range(n):
        l=int(input())
        c = []
        for i in range(l):
            temp=input()
            if(not(temp in c)):
                c.append(temp)

        print(len(c))



if __name__ == '__main__':
    main()