def main():
    N = int(input())
    numCard = list(map(int, input().split()))

    M = int(input())
    haveCard = list(map(int, input().split()))

    for i in haveCard:
        count = 0
        for j in numCard:
            if i == j:
                count += 1
        print(count, end = ' ')

if __name__ == "__main__":
    main()