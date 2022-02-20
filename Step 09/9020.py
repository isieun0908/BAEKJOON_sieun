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
    inputNum = int(input())

    for i in range(0, inputNum):
        case = int(input())

        for j in range(int(case/2), 0, -1):
            if checkPrime(j)==1 and checkPrime(case-j):
                print(j, case-j)



if __name__ == "__main__":
    main()