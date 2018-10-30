# https://open.kattis.com/problems/alphabetspam

def main():
    str = input()
    len=0
    whitespace=0
    lowercase = 0
    uppercase =0
    symbols = 0
    for i in str:
        char = ord(i)
        # print(i)
        len+=1;
        if(char>=65 and char<=90):
            uppercase+=1
        else:
            if(char>=97 and char<=122):
                lowercase+=1
            else:
                if(char==32 or char==9 or char ==95):
                    whitespace+=1
                else:
                    symbols+=1

    print(whitespace/len)
    print(lowercase/len)
    print(uppercase/len)
    print(symbols/len)



if __name__ == '__main__':
    main()
