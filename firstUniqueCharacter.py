#  Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
#
# Note: You may assume the string contain only lowercase letters.



def firstUniqChar(s):
    ch = []
    for i in set(s):
        if s.count(i) == 1:
            ch.append(s.index(i))
    if len(ch) > 0:
        return min(ch)
    else:
        return -1

print(firstUniqChar("loveleetcode"))