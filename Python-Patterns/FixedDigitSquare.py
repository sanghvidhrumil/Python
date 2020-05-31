n = int(input("Enter the number:"))
p = 1

for i in range(1, n+1):
    print('{} '.format(i) * n)

print('=' * 30)

while p < n+1:
    print('{} '.format(p) * n)
    p += 1

print('=' * 30)

# OR

for i in range(n):
    print((str(i + 1) + ' ') * n)
