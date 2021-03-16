while True:
    try:
        N1 = int(input("Please enter N1: "))
        N2 = int(input("Please enter N2: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

print(f"\nFinal Output")
print(f"The sum is: {N1+N2}")
print(f"The product is: {N1*N2}")
print(f"The division is: {N1/N2}")
print(f"The remainder is: {N1%N2}")