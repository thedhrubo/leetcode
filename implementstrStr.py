def strStr( haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    match = 0
    if len(needle)==0:
        return 0
    for i in range(0, len(haystack)-len(needle)+1):
        for j in range(0, len(needle)):
            if haystack[i+j] == needle[j]:
                match = match + 1
                if match == len(needle):
                    return i
            else:
                match = 0
                break
    return -1
print(strStr("mississippi","issip"))