if __name__ == '__main__':
    nums = list(map(int,input().split()))
    order=input()
    # print(order)
    nums.sort()
    # print(nums)
    a=0
    b=1
    c=2
    output=[]
    for ch in order:
        # print(ch)
        if(ch=='A'):
            # print(nums[a])
            output.append(nums[a])

        if(ch=='B'):
            # print(nums[b])
            output.append(nums[b])

        if(ch=='C'):
            # print(nums[c])
            output.append(nums[c])

    # print(output)

    for i in output:
        print(i,end="")
        print(" ",end="")

    print()