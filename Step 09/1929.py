def main():
    M, N = map(int, input().split())

    prime = {}

    for i in range(M, N+1):
        prime[i] = 1
    prime[1] = 0

    for i in range(2, N):
        loop = 2
        while i*loop <= N:
            prime[i*loop] = 0
            loop += 1

    for primeNum in prime.keys():
        if prime[primeNum]:
            print(primeNum)

if __name__ == "__main__":
    main()