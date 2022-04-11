def main():
    T = int(input())

    for t in range(0, T):
        n = int(input())

        wear = {}
        for tc in range(0, n):
            wear_name, wear_type = input().split()

            if wear_type in wear:
                wear[wear_type] += 1
            else:
                wear[wear_type] = 1

        print(wear)

if __name__ == "__main__":
    main()