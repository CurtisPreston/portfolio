def encode(input_string):
    count = 1
    prev = ''
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev,count)
                lst.append(entry)
                #print lst
            count = 1
            prev = character
        else:
            count += 1
    else:

        entry = (character,count)
        lst.append(entry)
        s=""
        for i in lst:
            s+=i[0]+str(i[1])
        return s


def decode(lst):
    q = ""
    for i in range(0,len(lst),2):
        q+=lst[i]*int(lst[i+1])
    return q


# Method call
if __name__ == '__main__':
    inp=input()
    cod=inp[0]
    inp=inp[2:len(inp)]

    if(cod=='E'):
        print(encode(inp))

    if (cod == 'D'):
        print(decode(inp))