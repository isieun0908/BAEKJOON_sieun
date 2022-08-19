import math
def lengthTest(sudoku, i, j):
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for index in range(9):
        if not index == j and not sudoku[i][index] == 0:
            num.remove(sudoku[i][index])
    if len(num) == 1:
        return num[0]
    else:
        return 0

def heightTest(sudoku, i, j):
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for index in range(9):
        if not index == j and not sudoku[index][j] == 0:
            num.remove(sudoku[index][j])
    if len(num) == 1:
        return num[0]
    else:
        return 0

def squareTest(sudoku, i, j):
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for indexI in range(0, 3):
        for indexJ in range(0, 3):
            inI = math.floor(i/3)*3 + indexI
            inJ = math.floor(j/3)*3 + indexJ
            if not (inI == i and inJ == j) and not sudoku[inI][inJ] == 0:
                num.remove(sudoku[inI][inJ])
    if len(num) == 1:
        return num[0]
    else:
        return 0

def printSudoku(sudoku):
    for line in sudoku:
        for i in line:
            print(i, end =' ')
        print()

def main():
    sudoku = []
    # 입력
    for i in range(0, 9):
        inputData = list(map(int, input().split()))
        sudoku.append(inputData)

    while True:
        flag = 1
        for i in range(9):
            for j in range(9):
                if sudoku[i][j] == 0:
                    flag = 0
                    # 가로
                    newValue = lengthTest(sudoku, i, j)
                    if newValue:
                        sudoku[i][j] = newValue
                        continue
                    # 세로
                    newValue = heightTest(sudoku, i, j)
                    if newValue:
                        sudoku[i][j] = newValue
                        continue
                    # 네모
                    newValue = squareTest(sudoku, i, j)
                    if newValue:
                        sudoku[i][j] = newValue
                        continue
        if flag:
            break

    # 출력
    printSudoku(sudoku)

if __name__ == "__main__":
    main()