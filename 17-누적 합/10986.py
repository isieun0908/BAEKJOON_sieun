import sys

def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    A = list(map(int, sys.stdin.readline().rstrip().split()))

    cumulative_sum = [0]
    sum = 0
    for a in A:
        sum += a
        cumulative_sum.append(sum)

    count = 0
    for i in range(1, N):
        for j in range(i, N+1):
            result = cumulative_sum[j] - cumulative_sum[i-1]
            if result % M == 0:
                count += 1
    print(count)
    
if __name__ == "__main__":
    main()