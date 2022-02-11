def main():
    M, N = map(int, input().split())

    for i in range(M, N+1):
        if not i == 1:
            flag = 1
            for j in range(2, i):
                if i%j == 0:
                    flag = 0
            if flag == 1:
                print(i)

if __name__ == "__main__":
    main()