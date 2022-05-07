A = int(input())
B = int(input())

sum = 0
weight = 1
while(B!=0):
    step = A*int(B%10)
    print(step)
    sum += step * weight
    B=int(B/10)
    weight *= 10
print(sum)