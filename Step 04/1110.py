import sys
input_num = int(sys.stdin.readline())
num = input_num

cycle = 0

while True:
    n1 = int(num / 10)
    n2 = num % 10

    num = n2*10 + (n1+n2)%10
    cycle += 1
    if num == input_num:
        break

print(cycle)