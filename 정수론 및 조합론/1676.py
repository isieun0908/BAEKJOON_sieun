def main():
    N = int(input())
    factorial = 1
    for i in range(1, N+1):
        factorial *= i

    factorial = str(factorial)

    count = 0
    for i in range(len(factorial)-1, -1, -1):
        if factorial[i] == '0':
            count += 1
        else:
            break
    print(count)

if __name__ == "__main__":
    main()