import sys

class Solution:
    def __init__(self) -> None:
        self.width = 0
        self.height = 0
        self.nodeDict = {}

    def solve(self):
        inputFile = open(sys.argv[1], "r")

        for line in inputFile:
            sanitizedLine = line.replace("\n", "")
            if self.width == 0:
                self.width = len(sanitizedLine)

            for index, char in enumerate(sanitizedLine):
                if char == "@":
                    locationStr = str(self.height) + "," + str(index)
                    self.nodeDict[locationStr] = []

                    # Check if there is an node to the left of it
                    self.connectNodes(locationStr, 0, index - 1)

                    # Jump to next row if we are the first row
                    if self.height == 0:
                        continue

                    # Check North
                    self.connectNodes(locationStr, -1, index)

                    # Check North West
                    if index != 0:
                        self.connectNodes(locationStr, -1, index - 1)

                    # Check North East
                    if index != 140:
                        self.connectNodes(locationStr, -1, index + 1)
                    
            self.height += 1

        inputFile.close()
        numOfAcceptableNodes = 0

        for x in self.nodeDict:
            if len(self.nodeDict[x]) < 4:
                numOfAcceptableNodes += 1

        print(numOfAcceptableNodes)
    
    def connectNodes(self, currentLocation, heightOffset, index):
        prevLocation = str(self.height + heightOffset) + "," + str(index)

        if prevLocation in self.nodeDict:
            if not (currentLocation in self.nodeDict[prevLocation]):
                self.nodeDict[prevLocation].append(currentLocation)
            
            if not (prevLocation in self.nodeDict[currentLocation]):
                self.nodeDict[currentLocation].append(prevLocation)

def main():
    solver = Solution()
    solver.solve()

if __name__ == "__main__":
    main()