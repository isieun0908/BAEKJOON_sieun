def main():
    N, K = map(int, input().split())

    binomialC = 1

    if not K == 0 and not K == N:
        numerator = N
        denominator = 1
        for i in range(1, K+1):
            binomialC *= numerator
            numerator -= 1
            denominator *= i
        binomialC /= denominator

    print(int(binomialC % 1000000007))

if __name__ == "__main__":
    main()