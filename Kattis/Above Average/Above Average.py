

if __name__ == '__main__':
        N=int(input())
        for x in range(N):
            nums=list(map(int,input().split()))
            nums=nums[1::]
            # print(nums)
            avg=sum(nums)/(len(nums))

            ab=0
            # print(avg)
            for e in nums:
                if e>avg:
                    ab+=1
                    # print(e,avg)
                # print()

            aavg=(ab/len(nums))*100000
            # print(aavg)
            aavg =round(aavg)
            aavg =aavg/1000
            aavg=format(aavg, '.3f')


            print(str(aavg)+"%")


