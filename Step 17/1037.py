def main():
    count = int(input())
    realDivisor = list(map(int, input().split()))

    pull_max = 1
    max = 0
    min = 1000001
    for i in range(0, count):
        pull_max *= realDivisor[i]
        if max < realDivisor[i]:
            max = realDivisor[i]
        if min > realDivisor[i]:
            min = realDivisor[i]

    divisor = 0
    for i in range(min*max, pull_max+1):
        flag = 1
        for j in range(0, count):
            if not i%realDivisor[j]==0:
                flag = 0
                break
        if flag==1:
            divisor = i
            break

    if count == 1:
        divisor = realDivisor[0] * realDivisor[0]

    if divisor==0:
        print(-1)
    else:
        print(divisor)

if __name__ == "__main__":
    main()