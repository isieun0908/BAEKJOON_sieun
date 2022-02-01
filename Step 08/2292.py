def main():
    num = int(input())
    count = 1

    compareValue = 1
    while compareValue < num:
        compareValue += 6*count
        count += 1

    print(count)
if __name__ == "__main__":
    main()