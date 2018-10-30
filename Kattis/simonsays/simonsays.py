


# https://open.kattis.com/problems/simonsays


N=int(input())

while(N>0):
    simon=input()

    if(simon[0:10]=="Simon says"):
        print(simon[11:len(simon)])
    N-=1