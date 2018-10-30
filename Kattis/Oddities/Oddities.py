def main():
    n=int(input())

    for x in range(n):
        num=int(input())
        if(num%2==0):
            print(num, "is even")
        else:
            print(num, "is odd")



if __name__ == '__main__':
    main()