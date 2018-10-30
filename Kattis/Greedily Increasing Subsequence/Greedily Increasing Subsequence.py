def main():
    N=int(input())
    numbs=list(map(int,input().split()))
    out=[]
    out.append(numbs[0])
    for x in numbs:
        if(x>out[len(out)-1]):
            out.append(x)

    print(len(out))
    for x in out:
        print(x," ",end="")

if __name__ == '__main__':
    main()