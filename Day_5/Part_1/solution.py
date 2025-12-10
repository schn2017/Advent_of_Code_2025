import sys

class Solution:
    def __init__(self) -> None:
        self.ranges = []

    def parseRange(self, line):
        parts = line.split("-")
        self.ranges.append([int(parts[0]), int(parts[1])])

    def solve(self):
        sum = 0
        inputFile = open(sys.argv[1], "r")

        for line in inputFile:
            sanitizedLine = line.rstrip()

            # skip any empty lines
            if len(sanitizedLine) == 0:
                continue

            if "-" in sanitizedLine:
                self.parseRange(sanitizedLine)
            else:
                val = int(sanitizedLine)
                for x in self.ranges:
                    if x[0] <= val and val <= x[1]:
                        sum += 1
                        break

        print("Sum is ", sum)

def main():
    solver = Solution()
    solver.solve()

if __name__ == "__main__":
    main()