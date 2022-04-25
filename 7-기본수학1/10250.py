def main():
    TestCase = int(input())
    for i in range(0, TestCase):
        H, W, N = map(int, input().split())
        floor = str(int(N % H))
        number = int(N / H) + 1
        if floor == "0":
            floor = str(H)
            number -= 1
        if number < 10:
            number = "0" + str(number)
        else:
            number = str(number)
        print(floor + number)

if __name__ == "__main__":
    main()