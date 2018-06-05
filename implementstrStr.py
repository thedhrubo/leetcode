# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
#
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#
# Clarification:
#
# What should we return when needle is an empty string? This is a great question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().




# I implemented the naive approach of string matching here.

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