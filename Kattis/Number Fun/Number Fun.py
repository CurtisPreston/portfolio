def main():
    def candiv(x,y,a):
        if(x/y==a):
            return True
        if(y/x==a):
            return True

        return False

    def canadd(x,y,a):
        if(x+y==a):
            return True
        return False

    def cansub(x,y,a):
        if(x-y==a):
            return True
        if(y-x==a):
            return True

        return False

    def canmul(x,y,a):
        if(x*y==a):
            return True
        return False


    def numcheak(x,y,a):
        
        if(canmul(x,y,a) or candiv(x,y,a) or cansub(x,y,a) or canadd(x,y,a)):
            return True
        return False

    n=int(input())

    for x in range(n):
        x,y,a = map(int, input().split())


        if(numcheak(x,y,a)):
            print("Possible")
        else:
            print("Impossible")





if __name__ == '__main__':
    main()