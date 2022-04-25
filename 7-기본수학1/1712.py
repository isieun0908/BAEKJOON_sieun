def main():
    A, B, C = map(int, input().split())

    if B < C:
        count = int(A / (C - B)) + 1
        print(count)
    else:
        print(-1)

if __name__ == "__main__":
    main()