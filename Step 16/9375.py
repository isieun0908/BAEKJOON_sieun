def main():
    T = int(input())

    for t in range(0, T):
        n = int(input())

        wear = []
        for tc in range(0, n):
            wear_name, wear_type = input().split()
            wear.append([wear_type, wear_name])
        print(wear)

if __name__ == "__main__":
    main()