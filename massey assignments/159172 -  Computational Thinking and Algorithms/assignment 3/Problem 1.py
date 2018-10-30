f = open("prob1.in")
inputlists=[]
for line in f:
    print(line)
    l = line.strip().split(' ')
    inputlists.append(l)

inputlists=[[int(y) for y in x] for x in inputlists]
print(inputlists)
k=inputlists[0][0]
inputlists.pop(0)



unsorted=[]
for x in range(k):
    unsorted.extend(inputlists[x])

def sorter(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sorter(less)+equal+sorter(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

print(unsorted)

sortedlist=sorter(unsorted)
print(sortedlist)
sortedstring=""
for x in sortedlist:
    sortedstring+=str(x)+" "

print(sortedstring)
output=open("prob1.out", 'w+')
output.write(sortedstring)

