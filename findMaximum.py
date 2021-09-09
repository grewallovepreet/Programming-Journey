#Find Maximum among the two numbers
def findMaximum (firstNumber, secondNumber):
    if firstNumber > secondNumber:
        print("firstNumber is greater")
        return firstNumber
    elif secondNumber > firstNumber:
        print("second number is greater")
        return secondNumber
    else:
        print("Both numbers are equal")
        return firstNumber

print("Enter the first number: ")
firstNumber = int(input())
print("Enter the second number:")
secondNumber = int(input())
maximumNumber = findMaximum(firstNumber, secondNumber)
print("Maximum Number = {}".format(maximumNumber))
