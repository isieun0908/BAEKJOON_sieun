def main():
    K, N = map(int, input().split())

    online = []
    sum = 0
    for i in range(K):
        inputData = int(input())
        online.append(inputData)
        sum += inputData

    for i in range(int(sum/N), 0, -1):
        count = 0
        for one_online in online:
            count += one_online // i
        if count >= N:
            print(i)
            break

if __name__ == "__main__":
    main()