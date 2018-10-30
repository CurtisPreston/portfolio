rate=[2,2.25,2.5,3,3.25,3.5,4,4.25,5,5.25,5.5]



print("Curtis Preston")
print("16453897")
print()
print()


def savings(rate,year):
    s=100*(1+((rate/100)/12))**(year*12)
    return s



print("\t\t\t\t**Savings on inital investment of $100.100**")
print("\t\t\t\tyears:",end=" ")
for x in range(0,10):
    print("\t  "+str(x+1),end=" ")
print(" ")
print("-"*102)
print("interest rate:",end="")


for x in range(0,len(rate)):
    if(rate[x]!=2):
        print("\t\t\t\t" + str('{:.2f}'.format(round(rate[x], 2))) + "%\t", end="")
    else:
        print("\t" + str(rate[x])+".00" + "%\t", end="")
    for year in range(1,11):
        print(str('{:.2f}'.format(round(savings(rate[x], year), 2))) +"\t",end="")
    print()
