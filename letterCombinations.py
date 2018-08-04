def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    dict = {}
    dict[2] = "abc"
    dict[3] = "def"
    dict[4] = "ghi"
    dict[5] = "jkl"
    dict[6] = "mno"
    dict[7] = "pqrs"
    dict[8] = "tuv"
    dict[9] = "wxyz"
    finalList = []
    characters = []
    for i in digits:
        str = dict[int(i)]
        for j in str:
            characters.append(j)

    def permutation(characters):
        if len(characters) == 0:
            return [[]]
        else:
            for x in characters:
                temp = characters[:]
                temp.remove(x)
                finalList.extend([[x] + r for r in permutation(temp)])
        return finalList
    permutation(characters)
    return finalList

print(letterCombinations("23"))