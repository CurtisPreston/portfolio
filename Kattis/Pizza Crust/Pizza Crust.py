import math

if __name__ == '__main__':
    R,C = map(int,input().split())

    Ra=(R**2)*math.pi


    Ca=((R-C)**2)*math.pi

    dif=Ra-Ca

    # print(dif)

    per = dif/Ra

    # print(per)

    if(per==0):
        print(format(100, '.6f'))

    elif(per==1):
        print(format(0, '.6f'))

    else:
        per = (1-per) *100
        print(format(per, '.6f'))