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

        for index, line in enumerate(inputFile):
            sanitizedLine = line.rstrip()
            parts = sanitizedLine.split(" ")

            partIdx = 0
            for part in parts:
                if len(part) == 0:
                    continue
                
                if index == 0:
                    newProblem = Problem()
                    self.problems.append(newProblem)
                
                if part.isnumeric():
                    self.problems[partIdx].addNumber(int(part))
                else:
                    self.problems[partIdx].setOperator(part)

                partIdx += 1

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