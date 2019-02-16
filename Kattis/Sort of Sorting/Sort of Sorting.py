#https://open.kattis.com/problems/sortofsorting
#writen by curtis preston 17/02/2019

while(True):
  names=[]
  #getting amount of names
  N=int(input())
  #if last input
  if(N==0):
    exit()
  #getting names
  for x in range(N):
    names.append(input())

  
  #sort name list by first 2 charactures
  names.sort(key=lambda x:x[:2])
 
  #display names
  for x in range(N):
    print(names[x])

  print()




