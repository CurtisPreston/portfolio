f = open("prob3.in")
inputlists=[]
for line in f:
    print(line)
    l = line.strip().split(' ')
    inputlists.append(l)

inputlists=[[int(y) for y in x] for x in inputlists]
k=inputlists[0][0]
inputlists.pop(0)
print(inputlists)
f.close()

cheak={}

istree = True


for x in inputlists:
    if(str(x[1]) in cheak.keys()):
        cheak[str(x[1])] +=1
    else:
        cheak[str(x[1])] =1


print(cheak)
print(cheak.values())

if({k:v for (k,v) in cheak.items() if v > 1}):
    istree = False
    print("is not a tree has non-root node with more than 1 incoming")




cheak={}
keys=[]

for x in inputlists:
    if(x[0] not in keys):
        keys.append(str(x[0]))

cheak={key: 0 for key in keys}

for x in inputlists:
    if (str(x[1]) in cheak.keys()):
        cheak[str(x[1])]+=1


count=(sum( x == 0 for x in cheak.values() ))

if(count>1):
    istree=False

print(istree)


file=open("prob3.out",'w+')
if(istree):
    file.write("this is a tree")
    print("this is a tree")
else:
    file.write("this is not a tree")
    print("this is not a tree")