# https://open.kattis.com/problems/babybites

def main():
    N=int(input())

    counting=input().split()
    fishy=False
    for i in range(1,len(counting)+1):

        if(str(i)==counting[i-1] or counting[i-1]=="mumble"):
            continue
        else:
            fishy=True


    if(fishy):
        print("something is fishy")
    else:
        print("makes sense")


if __name__ == '__main__':
    main()