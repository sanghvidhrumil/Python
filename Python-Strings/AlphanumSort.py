s = 'AB4A1D3'
alpha = []
digit = []
for x in s:
    if x.isalpha():
        alpha.append(x)
    if x.isdigit():
        digit.append(x)
j = ''.join(sorted(alpha) + sorted(digit))
print(j)
