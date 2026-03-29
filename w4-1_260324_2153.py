import sys

word = sys.stdin.readline().strip()
total = 0

for char in word:
    if 'a' <= char <= 'z':
        total += ord(char) - ord('a') + 1
    else:
        total += ord(char) - ord('A') + 27

def is_prime(n):
    if n == 1:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if is_prime(total):
    print("It is a prime word.")
else:
    print("It is not a prime word.")