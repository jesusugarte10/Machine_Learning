def main():
    print("Welcome to the College GPA Calculator\n")
    nClasses = int(input("How Many Classes are you taking: "))

    sum = 0
    score = 0
    for i in range(nClasses):
        hours = get_hours(i)
        sum = sum + hours
        score = score + ((hours/get_score(i))*4)
    print("\n\n## GPA IS: %.2f ##\n" %((sum/score)*4))

def get_score(i):
    print("\n  A    A-   B+   B    B-   C+   C    C-    F")
    print("(4.0)(3.7)(3.3)(3.0)(2.7)(2.3)(2.0)(1.70)(0.0)")
    print("")
    print("Please enter number in range")
    return value_Check(i)

def get_hours(i):
    print("------------------------------------------------")
    return float(input("\nHow many credit hours for class #%d: " %(i+1)))

def value_Check(i):

    x = float(input("Score for class #%d: " %(i+1)))
    while not(0 <= x <= 4):
        print("\n!!!WARNING!!!")
        x = float(input("Please Enter number within Grade Range \nScore for class #%d: " %(i+1)))
    return x

main()