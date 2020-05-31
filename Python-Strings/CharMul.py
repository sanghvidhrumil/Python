s = 'A4Z3D6'
out = ' '
x = ''
for ch in s:
    if ch.isalpha():
        x = ch
    else:
        d = int(ch)
        out += x * d

k=''.join(sorted(out))
print(k)