import sys

def pado(N):
    p = [0, 1, 1, 1, 2, 2]
    if N < 4:
        return 1
    elif N < 6:
        return 2
    
    for i in range(6, N+1):
        p.append(p[i-1] + p[i-5])
    
    return p[len(p)-1]

def main():
    T = int(sys.stdin.readline())

    for t in range(T):
        N = int(sys.stdin.readline())

        print(pado(N))

if __name__ == "__main__":
    main()