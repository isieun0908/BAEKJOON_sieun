def main():
    N = int(input())
    n_list = list(map(int, input().split()))
    M = int(input())
    m_list = list(map(int, input().split()))

    for m in range(0, M):
        if m_list[m] in n_list:
            print(1, end=' ')
        else:
            print(0, end=' ')

if __name__ == "__main__":
    main()