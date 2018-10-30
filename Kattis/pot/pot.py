def main():
    n=int(input())
    total=0
    for x in range(n):
        num=int(input())
        total+=pow((int(num/10)),(num%10))

    print(total)




if __name__ == '__main__':
    main()