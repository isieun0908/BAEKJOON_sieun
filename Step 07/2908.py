def main():
    number = input().split()

    for num in range(0, 2):
        newNum = ""
        for i in range(len(number[num]), 0, -1):
            newNum += number[num][i-1]
        number[num] = newNum
    if number[0] > number[1]:
        print(number[0])
    else:
        print(number[1])

if __name__ == "__main__":
    main()