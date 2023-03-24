import sys

def main():
    N = int(sys.stdin.readline())

    for i in range(0, int(N/4)):
        print("long ", end='')

    print("int")

if __name__ == "__main__":
    main()