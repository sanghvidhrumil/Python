n = int(input('Enter the number:'))
p = 0

for i in range(n):
    print(' ' * (n-i-1) + '* ' * (i+1))
print('=' * 30)
