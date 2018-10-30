def main():
    n = int(input())
    for x in range(n):
        g=int(input())
        guest=list(map(int,input().split()))
        # print(guest)
        count=0
        while count < len(guest):
            temp=guest[0]
            guest.pop(0)
            if(temp in guest):
                guest.append(temp)
            else:
                print("Case #"+str(x+1)+":",temp)
                break
            count +=1



if __name__ == '__main__':
    main()