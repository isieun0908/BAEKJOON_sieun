def main():
    number = int(input())
    loop = int(number / 5)
    if number%5 == 0:
        output = loop
    else:
        flag = 0
        for i in range(loop, -1, -1):
            gap = number - i*5
            rest = int(gap / 3)
            if gap%3 == 0:
                num_3 = i
                flag = 1
                break
        if flag == 0:
            output = -1
        else:
            output = num_3 + rest
    print(output)

if __name__ == "__main__":
    main()