import sys

inputFile = open(sys.argv[1], "r")

def isInvalid(number, min, max):
    return min <= number or number <= max

for line in inputFile:
    ranges = line.split(",")

    for range in ranges:
        rangeParts = range.split("-")
        min = int(rangeParts[0])
        max = int(rangeParts[1])

        minLen = len(rangeParts[0])
        maxLen = len(rangeParts[1])

        # If it an even length th
        if minLen % 2 == 0:
            midPoint = minLen // 2
            #print("midPoint", midPoint)
            firstHalf = rangeParts[0][:midPoint]
            
            dupNum = int(firstHalf + firstHalf)
            #print("The dup num is ", dupNum)
            pass
    
        if maxLen %2 == 0:
            pass

        # Basically all we want to do is only check even length ranges, an odd number can't be made of
        # duplicates
        # For even numbers we want to take the first half of the numerical string of the min and max
        # for example 1234XXXX - 5678XXXX
        # we would iterate from 1234 to 5678, if the number 1234 (first half) + 1234 (first half) is in the
        # min max range then we have an invalid id


        print("min str len: ", minLen, " parity: ", "even" if minLen % 2 == 0 else "odd")
        print("max str len: ", maxLen, " parity: ", "even" if maxLen % 2 == 0 else "odd")
        print("The difference between max and min", max - min)

        print(min)
        print(max)

        print()

def main():
    pass

if __name__ == "__main__":
  main()