import sys

def main():
    N, M = map(int, sys.stdin.readline().split())

    basket = [ i for i in range(N+1)]

    for m in range(M):
        i, j = map(int, sys.stdin.readline().split())
        part_basket = basket[i:j+1]
        part_basket.reverse()
        basket[i:j+1] = part_basket

    for i in range(1, N+1):
        print(basket[i], end=" ")

if __name__ == "__main__":
    main()