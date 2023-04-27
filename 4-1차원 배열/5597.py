import sys

def main():
    attendance = [0 for i in range(31)]

    print(attendance)
    for i in range(28):
        input = int(sys.stdin.readline().strip())

        attendance[input] = 1

    for i in range(1, len(attendance)):
        if attendance[i] == 0:
            print(i)


if __name__ == "__main__":
    main()