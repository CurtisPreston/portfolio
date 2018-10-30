def main():
    Gunnar=input().split()
    Emma = input().split()
    for x in range(len(Gunnar)):
        Gunnar[x]=int(Gunnar[x])
        Emma[x]  =int(Emma[x])


    GunnarS=sum(Gunnar)
    EmmaS = sum(Emma)

    if(EmmaS>GunnarS):
        print("Emma")
    elif(EmmaS<GunnarS):
        print("Gunnar")
    else:
        print("Tie")




if __name__ == '__main__':
    main()