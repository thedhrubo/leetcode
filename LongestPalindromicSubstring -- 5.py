# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
# Example 2:
#
# Input: "cbbd"
# Output: "bb"

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    maxstring = ""
    if s == s[::-1]:
        return s
    for i in range(0, len(s)):
        s1 = compareString(i, i, s)
        s2 = compareString(i, i + 1, s)
        if len(s1) >= len(maxstring):
            maxstring = s1
        if len(s2) >= len(maxstring):
            maxstring = s2
        if len(s) // 2 == i and len(s) - i < len(maxstring):
            break;
    return maxstring


def compareString(left, right, givenString):
    while left > -1 and right < len(givenString) and givenString[left] == givenString[right]:
        left = left - 1
        right = right + 1
    return givenString[left + 1:right]

print(longestPalindrome("ababababa"))