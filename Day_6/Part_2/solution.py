import sys

class Problem:
    def __init__(self) -> None:
        self.numbers = []
        self.operator = ""

    def addNumber(self, number: int):
        self.numbers.append(number)

    def setOperator(self, op: str):
        self.operator = op

class Solution:
    def __init__(self) -> None:
        self.problems: list[Problem] = []

    def solve(self):
        inputFile = open(sys.argv[1], "r")

        lines: list[str] = []
        opLine = -1
        for index, line in enumerate(inputFile):
            sanitizedLine = line.replace("\n", "")
            lines.append(sanitizedLine)

            if "*" in sanitizedLine or "+" in sanitizedLine:
                opLine = index

        opParts = lines[opLine].split(" ")
        for opPart in opParts:
            if len(opPart) == 0:
                continue

            newProblem = Problem()
            newProblem.setOperator(opPart)
            self.problems.append(newProblem)


        problemIdx = len(self.problems) - 1

        for x in range(len(lines[0]) - 1, -1, -1):
            numStr = ""
            for y in range(0, opLine):
                numStr += lines[y][x]

            sanitizedNumStr = numStr.replace(" ", "")
            if len(sanitizedNumStr) == 0:
                problemIdx -= 1
                continue

            self.problems[problemIdx].addNumber(int(sanitizedNumStr))

        sum = 0
        for problem in self.problems:
            if problem.operator == "*":
                product = 1

                for num in problem.numbers:
                    product *= num
                sum += product
            elif problem.operator == "+":   
                for num in problem.numbers:
                    sum += num
         
        print("The sum is", sum)

def main():
    solver = Solution()
    solver.solve()

if __name__ == "__main__":
    main()