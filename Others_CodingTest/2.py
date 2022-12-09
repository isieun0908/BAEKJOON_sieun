import sys

def solution(a, b, budget):
    answer = 0

    for i in range(int(budget/a)+1):
        print("i :", i)
        print("result : ", (budget - i * a) % b)
        if ( budget - (i * a) ) % b == 0:
            answer += 1

    return answer

def main():
    a, b, budget = map(int, sys.stdin.readline().rstrip().split())

    print(solution(a, b, budget))

if __name__ == "__main__":
    main()