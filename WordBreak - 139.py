# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# Note:
#
#     The same word in the dictionary may be reused multiple times in the segmentation.
#     You may assume the dictionary does not contain duplicate words.
#
# Example 1:
#
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
#
# Example 2:
#
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.
#
# Example 3:
#
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
#
# Now developing the naive solution
# time complexity is : O(n^n) for this test case : ["aaaaaaaaaag", ["a","aa","aaa","aaaa","aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
# space complexity : n depth recursion level for which O(n)

# def wordBreak(s, wordDict):
#     """
#     :type s: str
#     :type wordDict: List[str]
#     :rtype: bool
#     """
#
#     return wordBreakRecursion(s, 1, wordDict)
#
#
# def wordBreakRecursion(s, start, wordDict):
#     if start == len(s):
#         return True
#     for i in range(start, len(s)+1):
#         if s[start:i] in wordDict and wordBreakRecursion(s, i, wordDict):
#             return True
#     return False

# 2nd solution is with the memorization of the previous step by using dictionary
# Now the time complexity improved to O(n^2)

# def wordBreak(s, wordDict):
#     """
#     :type s: str
#     :type wordDict: List[str]
#     :rtype: bool
#     """
#     dict = {}
#     return wordBreakRecursion(s, 1, wordDict, dict)
#
#
# def wordBreakRecursion(s, start, wordDict, dict):
#     if start == len(s):
#         return True
#     if start in dict:
#         return dict[start]
#     for i in range(start, len(s)+1):
#         if s[start:i] in wordDict and wordBreakRecursion(s, i, wordDict, dict):
#             dict[start] = True
#             return True
#     dict[start] = False
#     return False

# We can also apply dynamic programming. Although the complexity will not be improved, we can learn how
# we need to divide the problems into sub problems in dynamic programming

print(wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
