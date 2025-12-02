import sys

# Number of times we pass the number 0 during a dial movement
numberPassingZero = 0

# Numver of times we land on the number zero after dial movement is complete
numberOfTimesAtZero = 0

# We start at 50
currentPosition = 50

# The size of the dial
dialSize = 100

inputFile = open(sys.argv[1], "r")

for line in inputFile:
    sanitizedLine = line.replace("\n", "")

    turnsToApply = 0
    if "R" in sanitizedLine:
        turnsToApply = int(sanitizedLine.split("R")[1])
    elif "L" in sanitizedLine:
        turnsToApply = -1 * int(sanitizedLine.split("L")[1])

    # Process any full rotations, starting and ending position are the same
    absoluteTurnsToApply = abs(turnsToApply) 

    if absoluteTurnsToApply > dialSize:
        # Integer division
        fullRotations = absoluteTurnsToApply // dialSize

        numberPassingZero += fullRotations
        
        # Calculate remaining turns after full rotations
        remainingTurns = absoluteTurnsToApply - (dialSize * fullRotations)
        if turnsToApply < 0:
            remainingTurns *= -1

        turnsToApply = remainingTurns

    newPosition = currentPosition + turnsToApply

    # If we are not at position 0 AND the new position is negative OR greater than 100 then we crossed 0
    if currentPosition != 0 and (newPosition < 0 or newPosition > 100):
        numberPassingZero += 1

    # Calculate the new position 
    currentPosition = newPosition % dialSize

    if currentPosition == 0:
        numberOfTimesAtZero += 1

inputFile.close()

print("Number of times landing on zero: ", numberOfTimesAtZero)
print("Number of times passing zero: ", numberPassingZero)
print("Total: ", numberOfTimesAtZero + numberPassingZero)