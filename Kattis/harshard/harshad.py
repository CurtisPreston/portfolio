#https://open.kattis.com/problems/harshadnumbers

def main():
  n=int(input())
  sn=n
  while not(isHarshad(sn)):
    sn+=1
  print(sn)
  



def isHarshad(number):
  n=number;
  s = 0
  while number:
    s += number % 10
    number //= 10
  if(n%s==0):
    return True

  return False





main()
