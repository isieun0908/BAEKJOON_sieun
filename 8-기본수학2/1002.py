def main():
    T = int(input())

    for i in range(0, T):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())

        # 두 좌표가 같을 때
        if x1 == x2 and y1 == y2:
            if r1 == r2:    # 무수히 많은 점
                print(-1)
            else:           # 못 만남
                print(0)
            continue

        JBdistance = ( (x2-x1)**2 + (y2-y1)**2 )**(1/2)

        # 두 점에서 만나는 경우
        if JBdistance > abs(r1-r2) and JBdistance < r1+r2:
            print(2)
        # 한 점에서 만나는 경우 : 외접, 내접
        elif JBdistance == r1+r2 or JBdistance == abs(r1-r2):
            print(1)
        else:
            print(0)

if __name__ == "__main__":
    main()