# https://open.kattis.com/problems/babelfish
import sys


def main():
    i="-"
    dic= dict();
    while(True):
        i=input()
        if(i==""):
            break
        word,trans=i.split()

        # print(word,trans)
        dic[trans]=word

    # print(dic)

    while (True):
        x=input()
        if (x.rstrip("\n") == ""):
            break
        s=x.rstrip("\n")
        if(s in dic.keys()):
            print(dic[s])
        else:
            print("eh")



if __name__ == '__main__':
    main()