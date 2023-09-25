#Positive negative checking 

Number = int(input("Enter the Number: "))

def positive_or_negative(Number):
    if Number >= 0:
        print("The given number is positive.")
    else:
        print("The given number is negative.")
        
positive_or_negative(Number)        
