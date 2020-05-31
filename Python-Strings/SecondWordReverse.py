s = 'One Two Three Four Five Six'
s1 = s.split()
print(s1)
i = 0
l1 = []
while i < len(s1):
    if i % 2 == 0:
        l1.append(s1[i])
    else:
        l1.append(s1[i][::-1])
    i += 1
print(l1)
