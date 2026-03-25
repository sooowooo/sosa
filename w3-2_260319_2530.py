A,B,C=map(int, input().split())
D=int(input())
total_seconds = A * 3600 + B * 60 + C + D
h = (total_seconds // 3600) % 24
m = (total_seconds // 60) % 60
s = total_seconds % 60
print(h, m, s)