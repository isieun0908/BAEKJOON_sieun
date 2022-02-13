def main():
    A, B, V = map(int, input().split())

    print(int((V-A)/(A-B)+1))

if __name__ == "__main__":
    main()
