# https://open.kattis.com/problems/drmmessages
# DRM Messages


def getcharvalue(char):
    value=ord(char)-65
    return value

def valuetochar(value):
    char = chr(value+65)
    return char

def stringtovalue(string):
    totals=0

    for x in string:
        totals+=getcharvalue(x)

    return totals



def total(s):
    value=0

    for x in s:
        v=ord(x)
        value+=v;

    return value

def shift(string, amount):
    outstring=""
    for c in string:
        val=getcharvalue(c)
        newval=val+amount

        while(newval>25):
            newval-=26

        newchar=valuetochar(newval)
        outstring+=newchar

    return outstring


def main():
    inp=input()

    half1=inp[0:int(len(inp)/2)]
    half2=inp[int(len(inp)/2):len(inp)]

    shiftedhalf1 = shift(half1, stringtovalue(half1))
    shiftedhalf2 = shift(half2, stringtovalue(half2))

    outstring=""

    for c in range(len(shiftedhalf1)):
        outstring+=shift(shiftedhalf1[c],getcharvalue(shiftedhalf2[c]))
        # print(outstring)
    print(outstring)

if __name__ == '__main__':
    main()