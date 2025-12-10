import sys

class IDRange:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def __str__(self):
        return f"{self.min}-{self.max}"

class Solution:
    def __init__(self) -> None:
        self.rangesDict = {}
        self.validIds = 0

    def parseRange(self, line):
        parts = line.split("-")
        min = int(parts[0])
        max = int(parts[1])

        newRange = IDRange(min, max)
        self.rangesDict[str(newRange)] = newRange

    def solve(self):
        inputFile = open(sys.argv[1], "r")

        for line in inputFile:
            sanitizedLine = line.rstrip()

            # skip any empty lines
            if len(sanitizedLine) == 0:
                continue

            if "-" in sanitizedLine:
                self.parseRange(sanitizedLine)

        failedMerges = 0
        rangesToDelete = []
        ranges = list(self.rangesDict.values())
        
        # Keep merging until we run out of ranges that can be merged
        while failedMerges != len(ranges):
            mergeFound = False

            # Remove any ranges that were merged into one range
            if len(rangesToDelete) > 0:
                for x in rangesToDelete:
                    if x in self.rangesDict:
                        del self.rangesDict[x]
                
                rangesToDelete = []

            # Get all remaining ranges
            ranges = list(self.rangesDict.values())

            # Sort them to make things easier
            ranges.sort(key=lambda idRange: idRange.min)

            for x in ranges:
                for y in ranges:
                    if str(x) == str(y):
                        continue
                    
                    # x fully contains y
                    if x.min <= y.min and y.max <= x.max:
                        mergeFound = True
                        rangesToDelete.append(str(y))
                    # y fully contains x
                    elif y.min <= x.min and x.max <= y.max:
                        mergeFound = True

                        rangesToDelete.append(str(x))
                    elif (x.min <= y.min and y.min <= x.max) and x.max <= y.max:
                        mergeFound = True

                        newRange = IDRange(x.min, y.max)
                        self.rangesDict[str(newRange)] = newRange
                        rangesToDelete.append(str(x))
                        rangesToDelete.append(str(y))

                    elif (y.min <= x.min and x.min <= y.max) and y.max <= x.max:
                        mergeFound = True

                        newRange = IDRange(y.min, x.max)
                        self.rangesDict[str(newRange)] = newRange
                        rangesToDelete.append(str(x))
                        rangesToDelete.append(str(y))
                    elif (x.min <= y.min and x.max == y.min - 1):
                        mergeFound = True

                        newRange = IDRange(x.min, y.max)
                        self.rangesDict[str(newRange)] = newRange
                        rangesToDelete.append(str(x))
                        rangesToDelete.append(str(y))

                    # Exit inner loop if a merge occurred
                    if mergeFound:
                        break

                # Exit outer loop if a merge occurred
                if mergeFound:
                    # Reset failed merge count if found a merge
                    failedMerges = 0
                    break
                else:
                    failedMerges += 1

        validIds = 0
        for x in ranges:
            # The difference plus 1 (to include the min value) is the amount of valid Ids per a given range
            validIds += x.max - x.min + 1

        print("Valid Ids", validIds)

def main():
    solver = Solution()
    solver.solve()

if __name__ == "__main__":
    main()