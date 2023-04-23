import sys

def main():
    N = int(sys.stdin.readline())

    RGB_list = []
    for n in range(N):
        RGB = list(map(int, sys.stdin.readline().split()))
        RGB_list.append(RGB)

    R = RGB_list[0][0]
    G = RGB_list[0][1]
    B = RGB_list[0][2]

    for i in range(1, N):
        new_R = min(G + RGB_list[i][0], B + RGB_list[i][0])
        new_G = min(R + RGB_list[i][1], B + RGB_list[i][1])
        new_B = min(R + RGB_list[i][2], G + RGB_list[i][2])
        R, G, B = new_R, new_G, new_B

    print(min(R, G, B))

if __name__ == "__main__":
    main()