



def main():
    t9={" ":0,"a":2,"b":22,"c":222,"d":3,"e":33,"f":333,"g":4,"h":44,"i":444,"j":5,"k":55,"l":555,"m":6,"n":66,"o":666,"p":7,"q":77,"r":777,"s":7777,"t":8,"u":88,"v":888,"w":9,"x":99,"y":999,"z":9999}

    n=int(input())
    for x in range(n):
        text=input()
        output=""
        for i in text:
            tmp=str(t9[i])
            if(len(output)>0):
                if(output[len(output)-1]==tmp[0]):
                    output+=" "
            output+=str(t9[i])

        print("Case #"+str(x+1)+":",output)







if __name__ == '__main__':
    main()