class Solution:
    def convert(self, s, numRows):
        result = [""] * numRows
        rowNumber = 0
        direction = 1

        for i in range(len(s)):
            result[rowNumber] = result[rowNumber] + s[i]
            if rowNumber < numRows - 1 and direction == 1:
                rowNumber += 1
            elif rowNumber > 0 and direction == -1:
                rowNumber -= 1
            else:
                direction *= -1
                rowNumber += direction

        return ''.join(result)
