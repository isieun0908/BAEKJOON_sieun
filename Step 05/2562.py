import sys

max = -1
for i in range(9):
    num = int(sys.stdin.readline())
    if num > max:
        max = num
        max_index = i+1
print(max)
print(max_index)