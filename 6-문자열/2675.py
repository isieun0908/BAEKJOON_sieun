def main():
    num = int(input())

    for repet in range(0, num):
        length, string = input().split(' ')
        length = int(length)
        for i in range(0, len(string)):
            for j in range(0, length):
                print(string[i], end='')
        print()

if __name__ == "__main__":
    main()