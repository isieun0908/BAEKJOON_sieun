import sys

def main():
    N, K = map(int, sys.stdin.readline().rstrip().split())
    temperature = list(map(int, sys.stdin.readline().rstrip().split()))

    sum_list = [0]
    sum = 0
    for i in temperature:
        sum += i
        sum_list.append(sum)
    
    max = -sys.maxsize
    for i in range(K, N+1):
        temperature_sum = sum_list[i] - sum_list[i-K]
        if temperature_sum > max:
            max = temperature_sum
    
    print(max)
    
if __name__ == "__main__":
    main()