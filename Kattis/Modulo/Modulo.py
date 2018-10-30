def main():
    Modulo=42
    nums=[]
    count=0
    set=[]
    for x in range(10):
        x=int(input())
        modu=x%Modulo
        if(modu not in set):
            set.append(modu)
    # print(nums)
    # print(count)
    # print(set)
    print(len(set))


if __name__ == '__main__':
    main()