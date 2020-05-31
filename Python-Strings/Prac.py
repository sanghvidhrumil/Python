s = 'A4B3C2'
x = ''
out = ''

for ch in s:
    if ch.isalpha():
        x = ch
    else:
        d = int(ch)
        out += x * d
print(out)
