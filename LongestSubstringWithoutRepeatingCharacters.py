# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    dict = {}
    start = 0
    returnValue = 0
    for i in range(0, len(s)):
        if s[i] in dict:
            index = dict[s[i]]
            if start <= index:
                start = index + 1
        dict[s[i]] = i
        returnValue = max(returnValue, i - start + 1)
    return returnValue

print(lengthOfLongestSubstring("abba"))