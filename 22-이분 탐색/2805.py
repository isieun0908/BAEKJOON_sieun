def main():
    N, M = map(int, input().split())
    tree = list(map(int, input().split()))

    maxHigh = max(tree)

    for h in range(maxHigh, 0, -1):
        lengthSum = 0
        for t in tree:
            if t > h:
                lengthSum += t - h
        if lengthSum >= M:
            print(h)
            break

if __name__ == "__main__":
    main()