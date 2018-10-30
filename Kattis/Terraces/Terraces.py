def main():
    def avg(x):
        count=0
        for i in x:
            count+=i
        av=count/len(x)
        return av

    def getD(x,y,grid):
        print(x,y)
        val = grid[x][y]
        # print(val)
        x1,xm1,y1,ym1=0,0,0,0
        out=""
        if(x+1<len(grid)):
            x1 = grid[x + 1][y]
            if(x1<val):
                out+='d'

        if(x-1>=0):
            xm1 = grid[x - 1][y]
            if(xm1<val):
                out+='u'

        if(y+1<len(grid[x])):
            y1 = grid[x][y + 1]
            if(y1<val):
                out+='r'

        if(y-1>=0):
            ym1=grid[x][y-1]
            if(ym1<val):
                out+'l'

        if(out==""):
            return True
        else:
            return False





    g=[]
    n=0
    x,y=map(int,input().split())
    for i in range(y):
        row=list(map(int,input().split()))
        g.append(row)

    d=[]

    for x in range(len(g)):
        row=[]
        for y in range(len(g[x])):
            i=getD(x,y,g)
            row.append(i)
        d.append(row)
        print(row)




if __name__ == '__main__':
    main()