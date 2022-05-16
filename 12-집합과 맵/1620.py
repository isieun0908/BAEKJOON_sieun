def main():
    N, M = map(int, input().split())

    poketmon = {}
    # 포켓몬 이름입력
    for num in range(0, N):
        inputData = input()
        poketmon[num+1] = inputData

    # 문제
    for i in range(0, M):
        inputData = input()
        if inputData[0] >= '0' and inputData[0] <= '9':
            inputData = int(inputData)
            print(poketmon[inputData])
        else:
            for key, value in poketmon.items():
                if value == inputData:
                    print(key)

if __name__ == "__main__":
    main()