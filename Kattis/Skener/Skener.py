# https://open.kattis.com/problems/skener


def main():
    Row,Col,RowZ,ColZ=map(int,input().split())

    image=[]
    for x in range(Row):
        i=input()
        image.append(i)
    if(ColZ>1):
        image=incressCol(image,ColZ)

    if(RowZ>1):
        image=incressRow(image,RowZ)


    printmatrix(image)

def incressCol(matrix,amount):
    matrixout=[]
    for row in matrix:
        newline=""
        for c in row:
            for x in range(amount):
                newline+=c
        matrixout.append(newline)
    return matrixout

def incressRow(matrix,amount):
    matrixout=[]
    for row in matrix:
        for x in range(amount):
            matrixout.append(row)
    return matrixout

def printmatrix(matrix):
    for row in matrix:
        print(row)


if __name__ == '__main__':
    main()