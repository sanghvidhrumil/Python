s = input('Enter the string:')
subs = input('Enter the substring:')
i = s.find(subs)
count = 0
if i == -1:
    print('{} substring not found'.format(subs))


while i != -1:
    count += 1
    print('{} found at index position {}'.format(subs, i))
    i = s.find(subs, i + len(subs), len(s))
print('Number of times {} occured is {}'.format(subs, count))
