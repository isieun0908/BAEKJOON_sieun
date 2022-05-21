def main():
    a, b = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_B = list(set(A) - set(B))
    B_A = list(set(B) - set(A))

    union = list(set(A_B) | set(B_A))
    print(len(union))

if __name__ == "__main__":
    main()