def main():
    H, M = map(int, input().split())
    plusM = int(input())

    M += plusM
    H += int(M / 60)
    M = M % 60
    H = H % 24
    print(H, M)

if __name__ == "__main__":
    main()