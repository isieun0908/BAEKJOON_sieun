def main():
    N = int(input())
    count = 0
    i=665
    while count < N:
        i += 1
        if "666" in str(i):
            count += 1
    print(i)

if __name__ == "__main__":
    main()