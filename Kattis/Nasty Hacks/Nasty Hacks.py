#https://open.kattis.com/problems/nastyhacks

def main():
    n=int(input())
    for e in range(n):
        r,a,c=map(int,input().split())
        # print(r,a-c)
        if(r<a-c):
            print("advertise")
        elif(r==a-c):
            print("does not matter")
        else:
            print("do not advertise")



if __name__ == '__main__':
    main()