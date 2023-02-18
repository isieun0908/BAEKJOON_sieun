import sys

def main():
    S = sys.stdin.readline().rstrip()
    q = int(sys.stdin.readline().rstrip())

    for i in range(0, q):
        line_q = sys.stdin.readline().rstrip().split()
        a = line_q[0]
        l = int(line_q[1])
        r = int(line_q[2])

        str = S[l:r+1]
        print(str.count(a))

if __name__ == "__main__":
    main()