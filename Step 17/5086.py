def main():

    while True:
        # 입력
        a, b = map(int, input().split())

        # 종료 조건
        if a==0 and b==0:
            break

        if b%a == 0:
            print("factor")
        elif a%b == 0:
            print("multiple")
        else:
            print("neither")


if __name__ == "__main__":
    main()