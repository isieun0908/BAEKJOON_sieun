num = int(input())
array = list(map(int, input().split()))

min = 1000001
max = -1000001
for i in range(num):
    if array[i] > max:
        max = array[i]
    if array[i] < min:
        min = array[i]

print(min, max)