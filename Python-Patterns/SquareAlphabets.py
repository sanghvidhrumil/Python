n = int(input("Enter the number:"))
p = 0

for i in range(n):
    print((chr(65 + i) + ' ') * n)

print('=' * 30)
while p < n:
    print((chr(65 + p) + ' ') * n)
    p += 1

