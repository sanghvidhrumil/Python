n = int(input("Enter the number:"))
p = 0

for i in range(n, 0, -1):
    print('* ' * i)

print('=' * 30)
for i in range(n):
    print('* ' * n)
    n -= 1
print('=' * 30)


for i in range(n):
    print('* ' * (n - i))
print('=' * 30)
while p < n:
    print('* ' * n)
    n -= 1
print()
