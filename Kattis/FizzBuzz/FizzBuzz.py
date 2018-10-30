def main():
    c=input()
    nums=c.split()
    for x in range(len(nums)):
        nums[x]=int(nums[x])

    for x in range(1,nums[2]+1,1):
        out=""
        if(x%nums[0]==0):
            out+="Fizz"
        if(x%nums[1]==0):
            out += "Buzz"
        if(out==""):
            out=x

        print(out)

if __name__ == '__main__':
    main()