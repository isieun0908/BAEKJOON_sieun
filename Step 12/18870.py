def main():
    N = int(input())
    x = list(map(int, input().split()))

    compression = {}
    for i in range(0, N):
        num = 0
        flag = 0
        for j in compression:
            if x[i] > j:
                num += 1
            elif x[i] == j:
                flag = 1
        if flag:
            continue
        if num == 0:
            for j in compression:
                compression[j] += 1
            compression[x[i]] = 0
        else:
            for j in compression:
                if j > x[i]:
                    compression[j] += 1
            compression[x[i]] = num

    for i in x:
        print(compression[i], end =' ')

if __name__ == "__main__":
    main()