def main():
    n=input()
    x=list(map(int,input().split()))
    # print(x)
    neg=0
    for i in x:
        if(i<0):
            neg+=1;

    print(neg)


if __name__ == '__main__':
    main()