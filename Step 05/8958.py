import sys

num = int(sys.stdin.readline())

for i in range(num):
    OX = sys.stdin.readline()
    total_score = 0
    accum_score = 0
    for j in range(len(OX)-1):
        if OX[j] == 'O':
            accum_score += 1
        else:
            accum_score = 0
        total_score += accum_score
    print(total_score)