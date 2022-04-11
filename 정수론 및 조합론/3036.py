import fractions

def main():
    N = int(input())
    r = list(map(int, input().split()))

    for i in range(1, len(r)):
        ring = fractions.Fraction(r[i], r[0])
        print(str(ring.denominator)+"/"+str(ring.numerator))

if __name__ == "__main__":
    main()