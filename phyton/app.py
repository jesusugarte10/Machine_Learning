def main():
    n = float(input("Please enter ammount in $$: "))
    func(n)

def func(n):

    quarter = 0
    dime = 0
    nickel = 0
    pennie = 0

    while n>0:
        if (n >= 0.25):
            quarter = quarter + 1
            n = n - 0.25
        elif (n >= 0.10):
            dime = dime +1 
            n = n - 0.1
        elif (n >= 0.05):
            nickel = nickel + 1
            n = n - 0.05
        else:
            pennie = pennie + 1
            n = n - 0.01
        n = round(n, 2)
        print(n)

    print(f'we need Q:{quarter} D:{dime} N:{nickel} P:{pennie}')

main()