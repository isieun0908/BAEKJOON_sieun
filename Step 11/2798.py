def main():
    N, M = map(int, input().split())
    card = list(map(int, input().split()))

    max = 0
    for i in range(0, N):
        one = card[i]
        for j in range(i+1, N):
            second = card[j]
            for k in range(j+1, N):
                third = card[k]
                sum = one+second+third
                if sum <= M and sum > max:
                    max = sum
    print(max)

if __name__ == "__main__":
    main()