#This program does handing exception for two numbers and prints multiple operarations
#I will Implement Float Data Type so that I can work with decimal numbers too!!

#While loop until True condition is broken
while True:
    #Try Except code block for exception handling
    try:
        #Try the two lines of codes if there is an exception, throw Value error exception
        N1 = float(input("Please enter N1: "))
        N2 = float(input("Please enter N2: "))
        #If code reaches here, there is no error
        break
    except ValueError:
        #If there is any expeption at any point, run this line of code
        print("Oops!  That was no valid number.  Try again...")

#Printing outputs
print(f"\nFinal Output")
print(f"The sum is: {N1+N2}")
print(f"The product is: {N1*N2}")
print(f"The division is: {N1/N2}")
print(f"The remainder is: {N1%N2}")