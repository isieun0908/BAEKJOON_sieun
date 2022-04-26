def main():
    N, M = map(int, input().split())

    numList = list(map(int, input().split()))

    for m in range(0, M):
        i, j = map(int, input().split())
        sum = 0
        for index in range(i-1, j):
            sum += numList[index]
        print(sum)

if __name__ == "__main__":
    main()