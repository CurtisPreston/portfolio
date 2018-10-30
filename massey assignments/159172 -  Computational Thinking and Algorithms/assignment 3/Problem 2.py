f = open("prob2.in")
inputlists=[]
for line in f:
    # print(line)
    l = line.strip().split(' ')
    inputlists.append(l)

#inputlists=[[int(y) for y in x] for x in inputlists]
# print(inputlists)k
k=int(inputlists[0][0])
inputlists.pop(0)
f.close()


print(inputlists)

for x in range(len(inputlists)):
    for y in range(len(inputlists[x])):
        try:
            inputlists[x][y]=int(inputlists[x][y])
        except ValueError:
            True


final=[]
removed=[]

for x in range(len(inputlists)):
    if(inputlists[x][0]=='insert'):
        final.append([inputlists[x][1],inputlists[x][2]])
    if (inputlists[x][0] == 'remove'):
        removed.append(final[0])
        final.pop(0)


print(final)

print(removed)

file=open('prob2.out','w+')
for x in range(len(removed)):
    file.writelines(str(removed[x][0])+" "+str(removed[x][1])+" \n")