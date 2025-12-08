import sys

class Solution:
    def __init__(self) -> None:
        self.width = 0
        self.height = 0
        self.nodeDict = {}

    def solve(self):
        inputFile = open(sys.argv[1], "r")

        self.width = 0
        self.height = 0

        self.nodeDict = {}

        for line in inputFile:
            sanitizedLine = line.replace("\n", "")
            if self.width == 0:
                self.width = len(sanitizedLine)

            for index, char in enumerate(sanitizedLine):
                if char == "@":
                    locationStr = str(self.height) + "," + str(index)
                    self.nodeDict[locationStr] = []

                    # Check if there is an node to the left of it
                    prevLocation = str(self.height) + "," + str(index - 1)
                    if prevLocation in self.nodeDict:
                        self.connectNodes(prevLocation, locationStr)

                    # Jump to next row if we are the first row
                    if self.height == 0:
                        continue

                    # Check North
                    prevLocation = str(self.height - 1) + "," + str(index)
                    if prevLocation in self.nodeDict:
                        self.connectNodes(prevLocation, locationStr)

                    # Check North West
                    prevLocation = str(self.height - 1) + "," + str(index - 1)

                    if index != 0 and prevLocation in self.nodeDict:
                        self.connectNodes(prevLocation, locationStr)

                    # Check North East
                    prevLocation = str(self.height - 1) + "," + str(index + 1)
                    if index != 140 and prevLocation in self.nodeDict:
                        self.connectNodes(prevLocation, locationStr)
                    
            self.height += 1

        inputFile.close()
        numOfAcceptableNodes = 0
        for x in self.nodeDict:
            if len(self.nodeDict[x]) < 4:
                numOfAcceptableNodes += 1

        print(numOfAcceptableNodes)
    
    def connectNodes(self, prevLocation, currentLocation):
        if not (currentLocation in self.nodeDict[prevLocation]):
            self.nodeDict[prevLocation].append(currentLocation)
        
        if not (prevLocation in self.nodeDict[currentLocation]):
            self.nodeDict[currentLocation].append(prevLocation)

def main():
    solver = Solution()
    solver.solve()

if __name__ == "__main__":
    main()