import sys

def main():
    # 값 입력받기
    N, M = map(int, sys.stdin.readline().split())

    # 바구니 값 초기화
    basket = [i+1 for i in range(N)]

    # 입력값에 따라 바구니 값 교환
    for i in range(M):
        i, j = map(int, sys.stdin.readline().split())

        basket[i-1], basket[j-1] = basket[j-1], basket[i-1]
    
    # 출력
    for item in basket:
        print(item, end=' ')

if __name__ == "__main__":
    main()