def main():
    N, M = map(int, input().split())

    S = []
    for i in range(0, N):
        inputData = input()
        S.append(inputData)

    count = 0
    for i in range(0, M):
        inputData = input()
        if inputData in S:
            count += 1
    print(count)

if __name__ == "__main__":
    main()