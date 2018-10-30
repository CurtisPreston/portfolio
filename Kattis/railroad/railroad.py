# https://open.kattis.com/problems/railroad2

def main():
    x,y=map(int,input().split())

    f=False;

    if((x*4+y*3)%2==0):
        f=True

    if(f):
        print("possible")
    else:
        print("impossible")
if __name__ == '__main__':
    main();