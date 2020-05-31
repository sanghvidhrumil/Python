n = int(input('Number of star squares: '))
p = 0

# for i in range(n):
#     print(i)
#     print(i, end=' ')

for i in range(n):
    print('* ' * n)
print('='*30)

while p <= n:
    print('* ' * n)
    p += 1

