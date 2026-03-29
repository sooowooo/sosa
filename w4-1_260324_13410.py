N, K = map(int, input().split())
results = []

for i in range(1, K + 1):
    val = str(N * i)
    reversed_val = int(val[::-1])
    results.append(reversed_val)

print(max(results))