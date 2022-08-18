def main():
    N, K = map(int, input().split())
    temperature = list(map(int, input().split()))

    max = -100
    for i in range(K-1, N):
        sumT = sum(temperature[i-(K-1):i+1])
        if sumT > max:
            max = sumT
    print(max)

if __name__ == "__main__":
    main()