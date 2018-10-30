
# https://open.kattis.com/problems/convexpolygonarea

# # input
# 2
# 3 1 1 2 1 2 2
# 4 0 0 10 0 13 5 10 8


# output

# 0.5
# 52


def main():
    n=int(input())
    for x in range(n):
        listp=list(map(int,input().split()))
        m=listp[0]
        listp.remove(listp[0])
        cords=[]

        for i in range(int(len(listp)/2)):
            point = [listp[i * 2],listp[(i * 2)+1]]
            cords.append(point)

        cords.append(cords[0])
        totall=0
        totalr=0
        for i in range(len(cords)-1):
            sum=cords[i][0]*cords[i+1][1]
            totall+=sum

        for i in range(len(cords)-1):
            sum=cords[i][1]*cords[i+1][0]
            totalr+=sum


        area=(totall-totalr)/2

        print(area)
if __name__ == '__main__':
    main()