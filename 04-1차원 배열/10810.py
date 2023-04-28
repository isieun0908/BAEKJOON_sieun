import sys

def main():
    N, M = map(int, sys.stdin.readline().split())

    list_ = [0] * N

    for i in range(M):
        i, j, k = map(int, sys.stdin.readline().split())
        list_[i-1:j] = [k] * (j-i+1)
    
    for i in list_:
        print(i, end=' ')

if __name__ == "__main__":
    main()