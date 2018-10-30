def main():
    c = input().split()
    c[0]=int(c[0])
    c[1]=int(c[1])
    rolls=[[i,0]for i in range(c[0]+1+c[1]+1)]
    for x in range(1,c[0]+1):
        for y in range(1,c[1]+1):
            t=x+y
            rolls[t][1]+=1


    rolls = sorted(rolls, key=lambda item: item[1], reverse=True)


    temp = rolls[0]
    print(temp[0])
    for x in range(1,len(rolls)):
        if(rolls[x][1]==temp[1]):
            print(rolls[x][0])
    

if __name__ == '__main__':
    main()