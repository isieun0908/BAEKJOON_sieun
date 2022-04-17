ef factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)

def main():
    N = int(input())

    print(factorial(N))

if __name__ == "__main__":
    main()