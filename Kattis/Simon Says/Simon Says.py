# https://open.kattis.com/problems/simon

def main():
    n=int(input())
    triger="simon says "
    for x in range(n):
        tmp=input()
        if(triger in tmp):
            print(tmp[len(triger):len(tmp)])
        else:
            print()




if __name__ == '__main__':
    main()
