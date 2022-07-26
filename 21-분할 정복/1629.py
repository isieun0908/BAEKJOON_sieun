import math

def main():
    A, B, C = map(int, input().split())
    half = math.floor(B/2)
    if B % 2 ==0:   # 짝수
        print(((A**half)**2)%C)
    else:
        print((((A**half)**2)*A)%C)

if __name__ == "__main__":
    main()