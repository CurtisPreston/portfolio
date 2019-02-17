#https://open.kattis.com/problems/freefood
#find amount of days that free food is on offer when given ranges of days with free food
N=int(input())

days=[]

for x in range(N):

  s,i=map(int,input().split())
  for day in range(s,i+1):#go through all days in range
    if(day not in days):
      days.append(day)#if day not added to days yet add it
  

print(len(days))#print ammount of days
