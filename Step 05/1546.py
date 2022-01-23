import sys

num = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))

max_ = max(score)
sum = 0
for i in range(num):
    sum += score[i]/max_*100

print(sum/num)