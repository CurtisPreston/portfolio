def main():
    def difr(n1,n2):
        r=n1-n2
        return r

    correct=[1,1,2,2,2,8]

    inp = list(map(int,input().split()))

    dif=[]

    for x in range(len(correct)):
        dif.append(difr(correct[x],inp[x]))
    # print(dif)

    for x in dif:
        print(str(x)+"    ",end="")

if __name__ == '__main__':
    main()