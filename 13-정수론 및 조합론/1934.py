def main():
    T = int(input())

    for i in range(0, T):
        A, B = map(int, input().split())
        a, b = A, B
        remainder = b % a
        while not remainder == 0:
            b = a
            a = remainder
            remainder = b % a
        greatestCommonDivisor = a
        leastCommonMultiple = int( (A*B)/greatestCommonDivisor )
        print(leastCommonMultiple)

if __name__ == "__main__":
    main()