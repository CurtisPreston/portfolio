def main():
    x,y = input().split()
    # print(x,y)
    x=x[::-1]
    y=y[::-1]
    # print(x)
    # print(y)

    if(x>y):
        print(x)
    else:
        print(y)

if __name__ == '__main__':
    main()