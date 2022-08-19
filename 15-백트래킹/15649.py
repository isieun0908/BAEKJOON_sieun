def main():
    N, M = map(int, input().split())
    numList = []
    for i in range(0, M):
        numList.append(1)

    while True:
        # 출력
        dupli = []
        isDupli = 1
        for i in range(0, M):
            if numList[i] in dupli:
                isDupli = 0
                break
            dupli.append(numList[i])

        if isDupli:
            for i in range(0, M):
                print(numList[i], end=' ')
            print()

        # 종료
        flag = 1
        for i in range(0, M):
            if not numList[i] == N:
                flag = 0
                break
        if flag:
            break

        # 증가
        numList[M-1] += 1
        for i in range(M-1, -1, -1):
            if numList[i] >= N + 1:
                numList[i] = 1
                numList[i-1] += 1

if __name__ == "__main__":
    main()