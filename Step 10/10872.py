def main():
    N = int(input())

    facN = 1
    for i in range(1, N+1):
        facN *= i
    print(facN)

if __name__ == "__main__":
    main()