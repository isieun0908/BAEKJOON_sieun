def main():
    while True:
        try:
            A, B = input().split()
            print(int(A)+int(B))
        except EOFError:
            break

if __name__ == "__main__":
    main()