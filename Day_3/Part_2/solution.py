import sys

class Solution:
    def solve(self):
        inputFile = open(sys.argv[1], "r")
        sum = 0

        for line in inputFile:

            sanitizedLine = line.replace("\n", "")

            largestIdx = -1
            largestVal = -1
            for index, value in enumerate(sanitizedLine):
                if (len(sanitizedLine) - index - 1) < 12:
                    break

                val = int(value)
                if val > largestVal:
                    largestVal = val
                    largestIdx = index

            foundVals = []

            startingPos = largestIdx + 1
            while len(foundVals) < 11:
                foundIdx = self.bleh(startingPos, 11 - len(foundVals), sanitizedLine)
                startingPos = foundIdx + 1
                foundVals.append(sanitizedLine[foundIdx])

            foundVal = str(largestVal)
            for x in foundVals:
                foundVal += str(x)
            
            sum += int(foundVal)
            print("The found value is", foundVal)
            print("The length of the found value is", len(foundVal))
        print("The answer is", sum)

    def bleh(self, startingPos, numRem, sanitizedLine):
        largestIdx = -1
        largestVal = -1
        #print("Starting pos", startingPos)
        #print("starting str val", sanitizedLine[startingPos])
        #print("Number remaining", numRem)

        for x in range(startingPos, len(sanitizedLine)):
            val = int(sanitizedLine[x])
            if val > largestVal:
                largestVal = val
                largestIdx = x

            if len(sanitizedLine) - x - 1 < numRem:
                #print("breaking early", x, numRem)
                break
        
        #print("returning val", largestVal)
        #print("returning idx", largestIdx)
        #print()

        return largestIdx


def main():
    solver = Solution()
    solver.solve()

if __name__ == "__main__":
    main()
