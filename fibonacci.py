numberOfIterationsInput = input("How many iterations should we run?  ")
numberOfIterations = int(numberOfIterationsInput)
if (numberOfIterations<1) or (numberOfIterations>20):
   print("Number of iterations must be between 1 and 20.")
sum = 1
previousNumber = 0
tempNumber = 0
currentIteration = 0
result = ""
while currentIteration<numberOfIterations:
    tempNumber = sum
    sum = sum + previousNumber
    previousNumber = tempNumber
    currentIteration += 1
    result = result + str(sum) + ", "
print(result[:-2])