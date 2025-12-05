import sys

sum = 0

inputFile = open(sys.argv[1], "r")

for line in inputFile:
    ranges = line.split(",")

    for rng in ranges:
        rangeParts = rng.split("-")
        min = int(rangeParts[0])
        max = int(rangeParts[1])

        for num in range(min, max + 1):
            numStr = str(num)
            numStrLen = len(numStr)

            # Skip the number if it is odd
            if numStrLen % 2 != 0:
                continue
            
            midPoint = numStrLen // 2
            firstHalf = numStr[:midPoint]
            secondHalf = numStr[midPoint:]

            if firstHalf == secondHalf:
                sum += num

inputFile.close()

print("Sum of the invalid ids: ", sum)