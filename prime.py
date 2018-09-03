highestNumberInput = input("How high should we go?  ")
highestNumber = int(highestNumberInput)
if (highestNumber<1) or (highestNumber>100):
   print("The hightest number must be between 1 and 100.")

# tod0 - keep editing from here
sum = 1
previousNumber = 0
tempNumber = 0
currentIteration = 0
values = []
while currentIteration<numberOfIterations:
    tempNumber = sum
    sum = sum + previousNumber
    previousNumber = tempNumber
    currentIteration += 1
    values.append(sum)
isFirst = True
result = ""
for value in values:
    if (not isFirst):
        result = result + ", "
    else:
        isFirst = False
    result = result + str(value)
print(result)

