# Here in this file I wanted to learn more about the permutation for which I am trying to implement different way of doing permutation


def permuation(s):
    permutationString = []
    if len(s)<1:
        return []
    elif len(s)<2:
        return [s]
    else:
        permutationCalculation(s, 0, permutationString)
        return permutationString


def permutationCalculation(s, start, permutationString):
    if start == len(s)-1:
        permutationString.append(s)
        return False
    else:
        for i in range(start, len(s)):
            tempStr = list(s)
            # print(tempStr[start])
            tempStr[start],tempStr[i] = tempStr[i], tempStr[start]
            permutationCalculation("".join(tempStr), start+1, permutationString)

def permutation2ndVersion(s):
    permutationString = []
    if len(s) < 1:
        return []
    if len(s) < 2:
        return [s]
    else:
        permutationString = permutationCalculation2nd(s)
        return permutationString
def permutationCalculation2nd(string):
    if len(string) == 1:
        return [string]
    temp = []
    for i in range(0,len(string)):
        remainString = string[:i] + string[i+1:]
        for j in permutationCalculation2nd(remainString):
            temp.append(string[i] + j)
    return temp

print(permutation2ndVersion("abc"))