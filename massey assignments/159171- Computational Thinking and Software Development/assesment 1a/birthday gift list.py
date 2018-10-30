print("Cutis Liam Knows Preston")
print("16453897")
print()
print()

def budget(y):
    x=len(y)
    x=x*10

def val(name):
    worth=(len(name))*10
    return worth

amount=int(input("how many people do you have to buy gifts for?"))

Name=[]
value=[]


for x in range(0, amount):
    out=input("enter name "+str(x)+":")
    Name.append(out)
    value.append(val(Name[x]))

print(Name)

for x in range(0, amount):
    print("The budget for",Name[x],"'s gift is ",value[x])

print("My total birthday gift budget is: $",sum(value))