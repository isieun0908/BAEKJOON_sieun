def main():
    N = input()
    list = []
    for i in N:
        list.append(int(i))
    list.sort(reverse = True)
    for i in range(0, len(list)):
        print(list[i], end='')

if __name__ == "__main__":
    main()