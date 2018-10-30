def main():
    for x in range(3):
        i=list(map(int,input().split()))
        x=i[0]
        y=i[1]
        dif=str(x-y)
        if(dif[0]=='-'):
            dif=dif[1:len(dif)]

        print(dif)




    if __name__ == '__main__':
        main()