def checkPrime(prime):
    flag = 0
    if prime == 1:
        return 0
    for i in range(2, prime):
        if prime % i == 0:
            flag = 1
            break
    if flag == 1:
        return 0
    else:
        return 1

def main():
    M = int(input())
    N = int(input())

    sum = 0
    flag = 0
    for i in range(N, M-1, -1):
        if checkPrime(i):
            flag = 1
            sum += i
            min = i

    if flag:
        print(sum)
        print(min)
    else:
        print(-1)
if __name__ == "__main__":
    main()