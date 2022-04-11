def main():
    a, b = map(int, input().split())

    leastCommonMultiple = 1
    greatestCommonDivisor = 1
    while True:
        flag = 1
        for i in range(2, min(a, b) + 1):
            if a%i == 0 and b%i ==0:
                leastCommonMultiple *= i
                a = int(a/i)
                b = int(b/i)
                flag = 0
                break
        if flag:
            break
    greatestCommonDivisor = leastCommonMultiple * a * b

    print(leastCommonMultiple)
    print(greatestCommonDivisor)

if __name__ == "__main__":
    main()