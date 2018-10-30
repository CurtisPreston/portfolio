

def main():
    n=int(input())

    for x in range(n):
        sounds = input().split()
        nonfoxsounds = []
        s=""
        while(not(s=="what does the fox say?")):
            s=input()
            an=s.split()
            sound=an[-1]
            nonfoxsounds.append(sound)

        out=[]
        for sound in sounds:
            if(not(sound in nonfoxsounds)):
                out.append(sound)

        for o in out:
            print(o,end="")
            print(" ",end="")

        print()



if __name__ == '__main__':
    main()