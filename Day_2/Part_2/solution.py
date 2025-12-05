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

            # Build and test the various sub strings
            subStr = ""
            for char in numStr:
                subStr += char

                testStr = numStr
                testStr = testStr.replace(subStr, "")
                
                # A number is invalid if the substr appears at least twice
                # AND if the replaced testStr has a length of 0
                if numStr.count(subStr) >= 2 and len(testStr) == 0:
                    sum += num
                    break

inputFile.close()

print("Sum of the invalid ids: ", sum)