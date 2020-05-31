s = 'AAAABBBCCZ'

previous = s[0]
i = 1
c = 1
out = ''
while i < len(s):
    if s[i] == previous:
        c += 1
    else:
        out += str(c) + previous
        previous = s[i]
        c = 1
    if i == len(s) - 1:
        out += str(c) + previous
    i += 1
print(out)