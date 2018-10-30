def main():
    votes=[]
    max = [0,0]
    for x in range(5):
        votes.append(input().split())
        for i in range(len(votes[x])):
            votes[x][i]=int(votes[x][i])

        votes[x]=sum(votes[x])
        if votes[x]>max[1]:
            max[1]=votes[x]
            max[0]=x+1


    print(max[0],max[1])






if __name__ == '__main__':
    main()