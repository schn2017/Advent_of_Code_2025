import sys

class Solution:
    def solve(self):
        inputFile = open(sys.argv[1], "r")
        sum = 0

        for line in inputFile:
            sanitizedLine = line.replace("\n", "")

            firstIdx = self.findLargestDigit(0, len(sanitizedLine) - 1, sanitizedLine)

            # firstIdx + 1 in order to skip the previously found inddex
            secondIdx = self.findLargestDigit(firstIdx + 1, len(sanitizedLine), sanitizedLine)

            sum += int(sanitizedLine[firstIdx] + sanitizedLine[secondIdx])

        inputFile.close()

        print("The sum is", sum)

    def findLargestDigit(self, startingIdx, endingIdx, strVal) -> int:
        maxVal = -1
        retVal = -1

        for x in range(startingIdx, endingIdx):
            val = int(strVal[x])
            if val > maxVal:
                maxVal = val
                retVal = x

        return retVal

def main():
    solver = Solution()
    solver.solve()

if __name__ == "__main__":
    main()