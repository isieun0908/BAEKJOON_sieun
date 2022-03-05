def main():
    N = int(input())

    for i in range(0, N):
        num = i
        sum = num
        while num >= 1:
            sum += num % 10
            num = int(num / 10)
        if sum == N:
            print(i)
            exit()
    print(0)

if __name__ == "__main__":
    main()