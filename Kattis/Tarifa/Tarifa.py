def main():
    mb=int(input())
    N=int(input())
    left=0
    for x in range(N):
        m=int(input())
        left+=mb-m
    # print(left)
    Np1=left+mb
    print(Np1)


if __name__ == '__main__':
    main()