import sys

numberOfTimesAtZero = 0

# We start at 50
currentPosition = 50

inputFile = open(sys.argv[1], "r")

for line in inputFile:
    sanitizedLine = line.replace("\n", "")

    if "R" in sanitizedLine:
        currentPosition += int(sanitizedLine.split("R")[1])
    elif "L" in sanitizedLine:
        currentPosition -= int(sanitizedLine.split("L")[1])

    currentPosition = currentPosition % 100

    if currentPosition == 0:
        numberOfTimesAtZero += 1

inputFile.close()

print("Number of zeros", numberOfTimesAtZero)