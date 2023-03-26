import sys

def main():
    N = int(sys.stdin.readline())

    list_ = list(map(int, sys.stdin.readline().split()))
    v = int(sys.stdin.readline())

    print(list_.count(v))

if __name__ == "__main__":
    main()