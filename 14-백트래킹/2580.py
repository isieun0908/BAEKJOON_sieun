def lengthTest(sudoku, i, j):
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(i, j, sudoku[i][j])
    for index in range(9):
        if not index == j and not sudoku[i][index] == 0:
            num.remove(sudoku[i][index])
    if len(num) == 1:
        return num[0]
    else:
        return 0

def heightTest(sudoku, i, j):
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(i, j, sudoku[i][j])
    for index in range(9):
        if not index == j and not sudoku[index][j] == 0:
            num.remove(sudoku[index][j])
    if len(num) == 1:
        return num[0]
    else:
        return 0

def printSudoku(sudoku):
    for i in sudoku:
        print(i)

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
                    printSudoku(sudoku)
        if flag:
            break

    # 출력
    printSudoku(sudoku)

if __name__ == "__main__":
    main()