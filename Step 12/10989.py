def main():
    N = int(input())

    numList = []
    for i in range(0, N):
        num = int(input())
        numList.append(num)

    numList.sort()

    for n in numList:
        print(n)

if __name__ == "__main__":
    main()