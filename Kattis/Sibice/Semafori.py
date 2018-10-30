def main():
    def red(R,G,T):
        to=R+G
        while T>to:
            T-=to
        if(T<R):
            return True
        else:
            return False

    n,l=list(map(int,input().split()))
    time=0;
    dis=0;
    last=0
    for x in range(n):
        D,R,G = list(map(int,input().split()))
        delta=D-dis
        time+=delta
        while(red(R,G,time)):
            time+=1;
        dis=D

    while(dis<l):
        time+=1
        dis+=1


    print(time)



if __name__ == '__main__':
    main()