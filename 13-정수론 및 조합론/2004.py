def main():
    n, m = map(int, input().split())

    denominator = 1
    numerator = 1
    num = n
    for i in range(0, m):
        numerator *= num
        num -= 1
    for i in range(m, 1, -1):
        denominator *= i

    nCr = str(int(numerator / denominator))

    count = 0
    for i in range(len(nCr)-1, -1, -1):
        if nCr[i] == '0':
            count += 1
        else:
            break
    print(count)

if __name__ == "__main__":
    main()