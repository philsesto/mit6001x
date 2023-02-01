mo = ''

for i in range(len(s)):
    temp = 0
    for j in range(len(s[i+1:])):
        if s[i+j+1] >= s[i+j]:
            temp += 1
            continue
        break
    if temp+1 > len(mo):
        mo = s[i:i+temp+1]

print('Longest substring in alphabetical order is: ' + mo)