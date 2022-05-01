def main():
    S = input()
    q = int(input())

    for i in range(0, q):
        line_q = input().split()
        a = line_q[0]
        l = int(line_q[1])
        r = int(line_q[2])

        str = S[l:r+1]
        print(str.count(a))

if __name__ == "__main__":
    main()