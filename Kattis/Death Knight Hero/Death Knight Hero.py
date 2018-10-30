def main():
    n=int(input())
    win=0
    for x in range(n):
        order=input()
        if(not("CD"in order)):
            win+=1;

    print(win)


if __name__ == '__main__':
    main()