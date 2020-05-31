s = 'Jay Jinendra'
s1 = s.split()
print(s1)
l = []

for word in s1:
    l.append(word[::-1])
print(l)