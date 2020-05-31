s = 'ABCABCABCA'
subs = 'z'

i = s.find(subs)
c = 0
while i != -1:
    c += 1
    print('{} is at index {}'.format(subs, i))
    i = s.find(subs, len(subs) + i, len(s))
    print('The count is {}'.format(c))
