#Find largest among three numbers
N1 = int(input("Enter Number1: "))
N2 = int(input("Enter Number2: "))
N3 = int(input("Enter Number3: "))

if N1 > N2 and N1 > N3:
    print("The given Number1 is the largest among the given numbers.")
elif N2 > N1 and N2 > N3:
    print("The given Number2 is the largest among the given numbers.")
elif N3 > N1 and N3 > N2:
    print("The given Number3 is the largest among the given numbers.")   
else:
    print("The given number are equal.")
