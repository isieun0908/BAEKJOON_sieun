import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

num = A*B*C

result = [0,0,0,0,0,0,0,0,0,0]

while num != 0:
    result[num%10] += 1
    num = int(num / 10)

for i in range(10):
    print(result[i])