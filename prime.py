def is_prime(number):
    "Returns true if the number is prime."
    if (number < 2):
        return False
    elif (number < 4):
        return True
    for value in range(2, number):
        if (number!=value) and (number % value == 0):
            return False
    return True

highestNumberInput = input("How high should we go?  ")
highestNumber = int(highestNumberInput)
if (highestNumber<1) or (highestNumber>100):
   print("The hightest number must be between 1 and 100.")
primes = []
for value in range(1, highestNumber):
    if (is_prime(value)):
        primes.append(value)
isFirst = True
results = ""
for value in primes:
    if (not isFirst):
        results = results + ", " + str(value)
    else:
        results = str(value)
        isFirst = False
print(results)


