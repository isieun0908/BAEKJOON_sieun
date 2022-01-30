def main():
    A, B, C = map(int, input().split())

    count = 0
    gap = (A+B*1 - C*1) - (A+B*2 - C*2)
    if gap < 0:
        count = -1
    while A+B*count >= C*count and count != -1:
        count += 1
    print(count)

if __name__ == "__main__":
    main()