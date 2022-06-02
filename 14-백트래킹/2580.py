#def lengthTest(sudoku, i, j):

#def heightTest(sudoku, i, j):

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
                print(sudoku[i][j])
                if sudoku[i][j] == 0:
                    flag = 0
                    sudoku[i][j] = -1
        if flag:
            break

    # 출력
    for i in sudoku:
        print(i)

if __name__ == "__main__":
    main()