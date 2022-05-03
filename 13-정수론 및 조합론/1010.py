def main():
    T = int(input())

    for i in range(0, T):
        N, M = map(int, input().split())
        Mfac = M
        for j in range(M-1, M-N, -1):
            Mfac *= j
        Nfac = N
        for j in range(N-1, 0, -1):
            Nfac *= j
        print(int(Mfac / Nfac))


if __name__ == "__main__":
    main()