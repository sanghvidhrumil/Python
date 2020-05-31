n = int(input("Enter the number:"))
p = 0

for i in range(n+1):
    print('* ' * i)

print('=' * 10)

while p < n+1:
    print('* ' * p)
    p += 1

print('=' * 10)
# OR
for i in range(n):
    for j in range(i + 1):
        print('*', end=' ')
    print()
