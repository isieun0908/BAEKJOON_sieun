def main():
    T = int(input())

    for t in range(T):
        p = input()
        N = int(input())
        if N == 0:
            print("error")
            break
        string = input()
        dqueue = list(map(int, string[1:len(string)-1].split(',')))

        flag = 1
        for command in p:
            if command == 'R':
                dqueue.reverse()
            elif command == 'D':
                if len(dqueue) == 0:
                    print("error")
                    flag = 0
                    break
                dqueue.pop(0)
        if flag:
            print(dqueue)

if __name__ == "__main__":
    main()