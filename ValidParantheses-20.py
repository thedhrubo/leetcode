# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#
# Note that an empty string is also considered valid.
#
# Example 1:
#
# Input: "()"
# Output: true
#
# Example 2:
#
# Input: "()[]{}"
# Output: true
#
# Example 3:
#
# Input: "(]"
# Output: false
#
# Example 4:
#
# Input: "([)]"
# Output: false
#
# Example 5:
#
# Input: "{[]}"
# Output: true


# def isValid(s):
#     """
#     :type s: str
#     :rtype: bool
#     """
#     stack = []
#     if len(s) < 1:
#         return True
#     for i in s:
#         if i == "(" or i == "{" or i == "[":
#             stack.append(i)
#         elif i == ")" or i == "}" or i == "]":
#             if len(stack) < 1:
#                 return False
#             else:
#                 if stack[-1] == "(" and i == ")":
#                     stack.pop(-1)
#                 elif stack[-1] == "{" and i == "}":
#                     stack.pop(-1)
#                 elif stack[-1] == "[" and i == "]":
#                     stack.pop(-1)
#                 else:
#                     return False
#     if len(stack) == 0:
#         return True
#     else:
#         return False

# Another Elegant way is :

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """

    stack = []
    parenthesis = {")" : "(", "}" : "{","]" : "["}
    for i in s:
        if i not in parenthesis:
            stack.append(i)
        elif i in parenthesis:
            if not stack:
                return False
            else:
                if parenthesis[i] == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
    return not stack

print(isValid("{[]}"))