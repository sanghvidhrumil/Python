s = 'durgasoft'
s1 = s.split()
le = []
lo = []
i = 0
print(s1)
while i < len(s):
    if i % 2 == 0:
        le.append(s[i])
    else:
        lo.append(s[i])
    i += 1
print(le)
print(lo)
