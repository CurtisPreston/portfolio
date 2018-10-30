def main():



    n=int(input())
    for i in range(n):
        text=""
        words=input()
        w=int(len(words)**0.5)

        grid=[]
        for i in range(w):
            grid.append(words[i*w:(i+1)*w])

        rgrid=[]


        for x in range(w-1,-1,-1):
            row=""
            for y in range(w):
                row+=grid[y][x]

            text+=row


        print(text)



if __name__ == '__main__':
    main()
