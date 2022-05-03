def main():
    M, N = map(int, input().split())

    numList = []
    for n in range(0, N):
        numList.append(n+1)

    while True:
        for n in range(0, N):
            print(numList[n], end=' ')
        print()

        end = 0
        index = N-1
        while True:
            numList[index] += 1
            if not numList[index] == N:
                end = 1
                break
            numList[index] = 1
            index -= 1
            if index == -1:
                break

        if end: break


if __name__ == "__main__":
    main()