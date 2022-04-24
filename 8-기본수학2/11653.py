def checkPrime(number):
    if number == 1:
        return 0
    for i in range(2, number):
        if not number%i:
            return 0
    return 1

def main():
    N = int(input())

    while not N == 1:
        for i in range(2, N+1):
            if N%i == 0 and checkPrime(i):
                print(i)
                N = int(N/i)
                break

if __name__ == "__main__":
    main()