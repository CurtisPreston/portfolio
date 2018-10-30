def numyo7(N):
    while (N >= 7):
        N -= 7

    return N

monthDays=[31,28,31,30,31,30,31,31,30,31,30,31]

Days=["Wednesday","Thursday","Friday","Saturday","Sunday","Monday","Tuesday"]

d,m=map(int,input().split())


dCount=0

for x in range(m-1):
    dCount+=monthDays[x]

dCount+=d

# print(dCount)
print(Days[numyo7(dCount)])



