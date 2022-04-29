def main():
    Count = int(input())
    Number = input()

    sum = 0
    for i in range(0, Count):
        sum += int(Number[i])
    print(sum)
if __name__ == "__main__":
    main()