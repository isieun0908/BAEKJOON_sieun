def main():
    N, M = map(int, input().split())

    LL = []
    for i in range(0, N):
        inputData = input()
        LL.append(inputData)
    for i in range(0, M):
        inputData = input()
        if inputData in LL:
            print(inputData)

if __name__ == "__main__":
    main()