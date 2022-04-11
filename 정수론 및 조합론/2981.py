def main():
    N = int(input())
    numList = []
    distance = []

    for i in range(0, N):       # 숫자 입력
        num = int(input())
        numList.append(num)
    numList.sort()      # 정렬
    for i in range(1, N):       # 숫자 간의 차 구하기
        dist = numList[i] - numList[i - 1]
        distance.append(dist)
    distance.append(numList[N-1]-numList[0])

    leastCommonMultiple = 1
    while True:
        flag = 1
        for i in range(2, min(distance)+1):     # 값들 중 현재 최소인 약수 구하기
            all_r_0 = 1
            for d in distance:                  # 모든 원소에 대해 나누었을 때 나머지 0인지 확인
                if not d%i == 0:
                    all_r_0 = 0
            if all_r_0 == 1:                    # 모든 원소에 대해 나누어 떨어진다면
                for d in range(0, N):           # 모든 원소의 값 나누어 업데이트
                    distance[d] = int(distance[d] / i)
                leastCommonMultiple *= i        # 최대공약수 업데이트
                flag = 0                        # 변경 일어남
                print(leastCommonMultiple, end=' ')
                break
        if flag:
            break

if __name__ == "__main__":
    main()