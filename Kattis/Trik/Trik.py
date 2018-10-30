if __name__ == '__main__':
    ca=input()
    cup=1

    for x in ca:
        if(x=='A'):
            if(cup==1):
                cup=2
            elif(cup==2):
                cup=1
        if(x=='B'):
            if(cup==2):
                cup=3
            elif(cup==3):
                cup=2
        if(x=='C'):
            if(cup==1):
                cup=3
            elif(cup==3):
                cup=1

    print(cup)