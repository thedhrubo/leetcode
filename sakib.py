
def sakib(s):
    max = 0
    list = []
    longIndex = 0
    for i in range(1, len(s)):
        if s[i] >= max:
            max = s[i]
            list = []
            longIndex = i
            list.append(i)
        elif s[i] < max and s[i]> s[i-1] :
            for j in range(longIndex, i):
                if s[j] < s[i]:
                    list.remove(j)
            list.append(i)
        elif s[i] < max and s[i] < s[i-1]:
            list.append(i)
    return list

print(sakib([1,2,5,3,4,6,2,4, 3]))