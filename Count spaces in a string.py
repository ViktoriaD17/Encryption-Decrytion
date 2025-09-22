# PROCEDURAL Programming
# caclAverage - now accepts THREE Paramters - from the line that called it 

def calcAverage(num1, num2, num3):     # PROCEDURE - does not return a value
    average = (num1 + num2 + num3)/3
    print(f"Average is: {average}")
    
    return average # Returns average to the line that called it

# SUBROUTINE - calclAverage() now a Function - it returns a value

def inputValues():
    num1 = int(input("Enter number:"))
    num2 = int(input("Enter number:"))
    num3 = int(input("Enter number:"))

    # Calls the subroutine with THREE parameters (num1, num2, num3)
    # this sends them to the new subroutine 
    avg = calcAverage(num1, num2, num3) # Calls the subroutine and stores the rurned value as 'avg'
    print(avg)
inputValues()   # starts the first subroutine




































































































