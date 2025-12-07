import sys

class Solution:
    def solve(self):
        inputFile = open(sys.argv[1], "r")
        sum = 0

        for line in inputFile:

            sanitizedLine = line.replace("\n", "")

            # Find the Starting Digit
            largestIdx = -1
            largestVal = -1
            for index, value in enumerate(sanitizedLine):

                # Make sure there are 11 characters remaining
                if (len(sanitizedLine) - index - 1) < 11:
                    break

                val = int(value)
                if val > largestVal:
                    largestVal = val
                    largestIdx = index

            # Add the first digit to the list of values
            foundVals = [str(largestVal)]

            # Find the remaining 11 digits
            startingPos = largestIdx + 1
            while len(foundVals) < 12:
                foundIdx = self.findNextMaxValueIdx(startingPos, 12 - len(foundVals), sanitizedLine)

                # Set starting position to the index after the found one
                startingPos = foundIdx + 1
                foundVals.append(sanitizedLine[foundIdx])
            foundVal = "".join(foundVals)
            sum += int(foundVal)

        print("The answer is", sum)

    def findNextMaxValueIdx(self, startingPos, numRem, sanitizedLine):
        largestIdx = -1
        largestVal = -1

        for x in range(startingPos, len(sanitizedLine)):
            val = int(sanitizedLine[x])
            if val > largestVal:
                largestVal = val
                largestIdx = x

            # Stop looping if we have run out of characters to loop
            if len(sanitizedLine) -  1 - x < numRem:    
                break
        
        return largestIdx

def main():
    solver = Solution()
    solver.solve()

if __name__ == "__main__":
    main()

