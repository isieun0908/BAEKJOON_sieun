def main():
    T = int(input())

    for t in range(0, T):
        n = int(input())

        # 입력받아 dictionary에 저장
        wear = {}
        for tc in range(0, n):
            wear_name, wear_type = input().split()
            if wear_type in wear:
                wear[wear_type] += 1
            else:
                wear[wear_type] = 1

        # 경우의 수 세기
        # [각 종류의 옷 + 1(선택X)]를 모두 곱한 후,
        # 아무것도 안 입는 경우 -1하기
        cases = 1
        for case in wear.values():
            cases *= case + 1
        print(cases - 1)

if __name__ == "__main__":
    main()