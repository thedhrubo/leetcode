# Given an input string , reverse the string word by word.
#
# Example:
#
# Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
#
# Note:
#
#     A word is defined as a sequence of non-space characters.
#     The input string does not contain leading or trailing spaces.
#     The words are always separated by a single space.
#
# Follow up: Could you do it in-place without allocating extra space?


def reverseWords(s):
    start = 0
    boolVal = False
    s = reverseString(0, len(s)-1, s)
    for i in range(0,len(s)):
        if boolVal == False:
            start = i
            boolVal = True
        if s[i] == " ":
            s = reverseString(start,i-1, s)
            boolVal = False
    return s

def reverseString(fromIndex, to, givenString):
    while fromIndex < to:
        temp = givenString[fromIndex]
        givenString[fromIndex] = givenString[to]
        givenString[to] = temp
        fromIndex = fromIndex + 1
        to = to - 1
    return givenString

def reverseWordsShortestSolution(str):
    s = "".join(str)
    s = s.split(" ")[::-1]
    sr = ' '.join(s)
    str[:] = sr
    # for n in range(len(str)):
    #     str[n] = sr[n]
    # s = " ".join(s)
    return str

print(reverseWordsShortestSolution(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]))