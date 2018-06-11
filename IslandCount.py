# Number of Islands

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
#
# Example 2:
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3



def get_number_of_islands(binaryMatrix):
    pass # your code goes here
    count = 0

    def identifyAdjacent(eachRow, eachColumn, rowLength, columnLength):
        if eachRow >= 0 and eachRow < rowLength and eachColumn >= 0 and eachColumn < columnLength and binaryMatrix[eachRow][eachColumn] == 1:
            binaryMatrix[eachRow][eachColumn] = 2
            identifyAdjacent(eachRow-1, eachColumn, rowLength, columnLength)
            identifyAdjacent(eachRow+1, eachColumn, rowLength, columnLength)
            identifyAdjacent(eachRow, eachColumn-1, rowLength, columnLength)
            identifyAdjacent(eachRow, eachColumn+1, rowLength, columnLength)


    for eachRow in range(0,len(binaryMatrix)):
        for eachColumn in range(0, len(binaryMatrix[eachRow])):
            if binaryMatrix[eachRow][eachColumn] == 1:
                count += 1
                identifyAdjacent(eachRow, eachColumn, len(binaryMatrix), len(binaryMatrix[eachRow]))
    return count

binaryMatrix = [ [0,    1,    0,    1,    0],
                         [0,    0,    1,    1,    1],
                         [1,    0,    0,    1,    0],
                         [0,    1,    1,    0,    0],
                         [1,    0,    1,    0,    1] ]
print(get_number_of_islands(binaryMatrix))
