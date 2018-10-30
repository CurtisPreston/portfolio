#todo https://open.kattis.com/problems/unlockpattern



def main():
    inp=[]
    for x in range(3):
        i=list(map(int,input().split()))
        inp.append(i)


    order=[]
    for i in range(1,10):

        for x in range(len(inp)):
            for y in range(len(inp)):
                if(inp[x][y]==i):
                    order.append([x,y,i])


    lenth=0
    for x in range(len(order)-1):

        l=((order[x][0]-order[x+1][0])**2+(order[x][1]-order[x+1][1])**2)**0.5
        lenth+=l

    print(lenth)


if __name__ == '__main__':
    main()