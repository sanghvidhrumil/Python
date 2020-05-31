# Slice operator

s = ' dhrumil'
# print(s[::-1])

# Reverse Function
opt = reversed(s)
# for ch in opt:
#     print(ch,end='')
# print()
l1 = ''.join(opt)
print(l1)

# While loop

s1 = len(s) - 1
while s1 >= 0:
    print(s[s1], end='')
    s1 -= 1
