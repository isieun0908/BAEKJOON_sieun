def main():
    N = int(input())

    list = []
    for i in range(0, N):
        num = int(input())
        list.append(num)

    maxN = max(list)
    M = []
    for i in range(2, maxN+1):
        flag = 1
        remainder = list[0] % i
        for j in list:
            if not j % i == remainder:
                flag = 0
                break
        if flag:
            M.append(i)

    for i in M:
        print(i, end = ' ')

if __name__ == "__main__":
    main()