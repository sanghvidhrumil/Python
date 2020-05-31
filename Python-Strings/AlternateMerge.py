s = 'drml'
s1 = 'hui'
i, j = 0, 0
output = ''
while i < len(s) or j < len(s1):
    if i < len(s):
        output += s[i]
        i += 1
    if j < len(s1):
        output += s1[j]
        j += 1
print(output)

# stri = ''
# i, j = 0, 0
#
# while i < len(s) or j < len(s1):
#     stri += s[i] + s1[j]
#     i += 1
#     j += 1
# print(stri)
