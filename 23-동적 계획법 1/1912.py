import sys

def main():
    n = int(sys.stdin.readline())
    list_ = list(map(int, sys.stdin.readline().split()))

    sum_v = [list_[0]]

    for i in range(1, n):
        sum_v.append(max(sum_v[i-1] + list_[i], list_[i]))
    print(max(sum_v))

if __name__ == "__main__":
    main()