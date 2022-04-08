def main():
    N = int(input())

    M = []
    for n in range(0, N):
        m = int(input())
        M.append(m)
    print(M)

    greatestCommonDivisor = 1

    while True:
        end = 0
        minM = min(M)
        #print("min", minM)
        for i in range(2, minM+1):
            #print(i)
            flag = 0
            for j in M:
                if j % i == 0:
                    flag += 1
                    break
            if flag == N-1:
                print(i)
                for n in range(0, N):
                    M[n] = int(M[n] / i)
                greatestCommonDivisor *= i
                break
            if flag == 0:
                end = 1
        if end == 1:
            break
    print("최대공약수 : ", greatestCommonDivisor)

if __name__ == "__main__":
    main()