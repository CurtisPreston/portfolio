def main():
    N,W,H = map(int,input().split())
    D=(W**2+H**2)**0.5
    for x in range(N):
        L=int(input())
        if(L<=D):
            print("DA")
        else:
            print("NE")




if __name__ == '__main__':
    main()