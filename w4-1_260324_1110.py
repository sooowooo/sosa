N = int(input())
num = N
count = 0

while True:
    ten = num // 10
    one = num % 10
    total = ten + one
    
    num = (one * 10) + (total % 10)
    count += 1
    
    if num == N:
        break

print(count)