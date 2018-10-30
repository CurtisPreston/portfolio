def main():
    def Adrian(i):
        a=('A', 'B', 'C')
        x=i%len(a)
        return a[x]

    def Bruno(i):
        b=('B', 'A', 'B', 'C')
        x=i%len(b)
        return b[x]

    def Goran(i):
        g=('C', 'C', 'A', 'A', 'B', 'B')
        x=i%len(g)
        return g[x]

    num=int(input())
    score=[[i,0]for i in ["Adrian","Bruno","Goran"]]
    ans=input()

    for x in range(len(ans)):
        if (ans[x] == Adrian(x)):
            score[0][1]+=1
        if (ans[x] == Bruno(x)):
            score[1][1]+=1
        if (ans[x] == Goran(x)):
            score[2][1]+=1

    pr=[]
    pr.append(score[0])

    for x in score[1:len(score)]:
        if(x[1]>pr[0][1]):
            pr=[x]
        elif(x[1]==pr[0][1]):
            pr.append(x)

    print(pr[0][1])
    for x in pr:
        print(x[0])





if __name__ == '__main__':
    main()