# Bela
# https://open.kattis.com/problems/bela



if __name__ == '__main__':
    cards={"A":[11,11],"K":[4,4],"Q":[3,3],"J":[20,2],"T":[10,10],"9":[14,0],"8":[0,0],"7":[0,0]}
    # for i in sys.stdin:
    N,H=input().split()
    val=0
    for i in range(int(N)*4):
        e=input()
        # print(e)
        if(e[1]==H):
            tv=cards[e[0]][0]
            val += tv
        else:
            tv = cards[e[0]][1]
            val+=tv
    print(val)
