# https://open.kattis.com/problems/owlandfox
# input
# 4
# 30
# 199
# 1000
# 1520
#
# output
# 20
# 198
# 0
# 1510


def main():
    n=int(input())

    while(n>0):
        s=input()
        o=[]
        d=True
        for i in range(len(s)):
            if(int(s[len(s)-1-i])>0 and d):
                o.append(int(s[len(s)-1-i])-1)
                d=False
            else:
                o.append(s[len(s)-1-i])
        o.reverse()

        st=""
        for c in o:
            st+=str(c)

        ist=int(st)

        print(ist)

        n -= 1






if __name__ == '__main__':
    main();