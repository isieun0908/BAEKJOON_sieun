import sys

count = 0

rest = []

for i in range(10):
    num = int(sys.stdin.readline())
    num %= 42
    flag = 0
    for j in range(len(rest)):
        if rest[j] == num:
            flag = 1
    if flag == 0:
        rest.append(num)
        count += 1
print(count)