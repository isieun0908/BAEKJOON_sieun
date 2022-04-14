def main():
    n, m = map(int, input().split())

    nFac = 1
    rFac = 1
    n_rFac = 1
    for i in range(1, n+1):
        nFac *= i
    for i in range(1, m+1):
        rFac *= i
    for i in range(1, n-m+1):
        n_rFac *= i

    nCr = str(int(nFac / (rFac * n_rFac)))

    count = 0
    for i in range(len(nCr)-1, -1, -1):
        if nCr[i] == '0':
            count += 1
        else:
            break
    print(count)

if __name__ == "__main__":
    main()