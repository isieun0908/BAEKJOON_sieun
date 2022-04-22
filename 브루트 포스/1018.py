def countRecolor(chess):
    startW = 0
    startB = 0
    for n in range(0, 8):
        for m in range(0, 8):
            if n % 2 == 0:
                if m % 2 == 0:
                    if not chess[n][m] == "W":
                        startW += 1
                    else:
                        startB += 1
                else:
                    if not chess[n][m] == "B":
                        startW += 1
                    else:
                        startB += 1
            else:
                if m % 2 == 0:
                    if not chess[n][m] == "B":
                        startW += 1
                    else:
                        startB += 1
                else:
                    if not chess[n][m] == "W":
                        startW += 1
                    else:
                        startB += 1
    return min(startW, startB)

def main():
    N,M = map(int, input().split())

    chess = []
    for n in range(0, N):
        line = input()
        chess.append([])
        for wb in line:
            chess[n].append(wb)

    changeColor = 80

    for n in range(0, N-7):
        for m in range(0, M-7):
            chess_8 = []
            for i in range(0, 8):
                chess_8.append(chess[n+i][m:m+8])
            changeColor = min(changeColor, countRecolor(chess_8))
    print(changeColor)

if __name__ == "__main__":
    main()