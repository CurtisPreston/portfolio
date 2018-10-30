def main():
    priceP = float(input())
    nfeilds=int(input())

    price=0


    for x in range(nfeilds):
        temp = input().split()
        num = (float(temp[0]),float(temp[1]))
        size= num[0]*num[1]
        fprice=size*priceP
        price+=fprice

    print(price)

if __name__ == '__main__':
    main()