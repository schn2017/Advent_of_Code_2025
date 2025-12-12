import sys

class Solution:
    def __init__(self) -> None:
        pass

    def solve(self):
        inputFile = open(sys.argv[1], "r")
        for  line in inputFile:
            sanitizedLine = line.replace("\n", "")
            print(sanitizedLine)

def main():
    solver = Solution()
    solver.solve()

if __name__ == "__main__":
    main()