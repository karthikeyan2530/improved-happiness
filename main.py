def CheckLeap(Year):
    # Checking if the given year is a leap year
    if ((Year % 400 == 0) or
        (Year % 100 != 0) and
        (Year % 4 == 0)):
        print("Given Year is a leap Year")
    else:
        print("Given Year is not a leap year")

# Taking an input year from the user
Year = int(input("Enter the number: "))
# Printing the result
CheckLeap(Year)