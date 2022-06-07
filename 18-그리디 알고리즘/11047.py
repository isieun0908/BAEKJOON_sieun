def main():
    N, K = map(int, input().split())

    type = []
    for i in range(N):
        inputData = int(input())
        type.append(inputData)
    type.sort()

    count = 0
    for i in range(N-1, -1, -1):
        num = int( K/type[i] )
        if not num == 0:
            K -= num * type[i]
            count += num
    print(count)

if __name__ == "__main__":
    main()