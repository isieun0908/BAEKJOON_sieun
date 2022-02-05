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
    TestCase = int(input())

    count = 0
    prime = list(map(int, input().split()))

    for i in range(0, TestCase):
        if checkPrime(prime[i]):
            count += 1
    print(count)

if __name__ == "__main__":
    main()