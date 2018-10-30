# Cetvrta
# https://open.kattis.com/problems/cetvrta

if __name__ == '__main__':
    cords=[]
    for i in range(3):
        e=list(map(int,input().split()))
        cords.append(e)

    x1=1001
    y1=1001
    x2=0
    y2=0

    for x in range(3):
        e=cords[x]
        if(e[0]<x1):
            x1=e[0]
        if(e[1]<y1):
            y1=e[1]

        if(e[0]>x2):
            x2=e[0]

        if(e[1]>y2):
            y2=e[1]

    # print(x1,x2,y1,y2)
    # print(cords)

    if(not([x1,y1] in cords)):

        print(x1,y1)

    if(not([x2,y1] in cords)):

        print(x2,y1)

    if(not([x1,y2] in cords)):

        print(x1,y2)

    if(not([x2,y2] in cords)):

        print(x2,y2)
