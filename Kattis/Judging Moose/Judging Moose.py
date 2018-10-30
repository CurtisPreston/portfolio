# Judging Moose
# https://open.kattis.com/problems/judgingmoose


if __name__ == '__main__':
        a1,a2=map(int,input().split())

        # print(a1,a2)

        if(a1==a2):
            if (a1 == 0 and a2 == 0):
                print("Not a moose")
                exit()

            print("Even",a1*2)
            exit()

        print("Odd", max(a1,a2) * 2)
        exit()
