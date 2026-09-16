print("Leap Year Detector")
year_input = input("Please enter a year: ")
try:
    year = int(year_input)
except Error:
    print("Error: Please enter a valid whole number.")
    exit()
if (year % 400 == 0):
    print(f"\n{year} is a leap year.")
elif (year % 4 == 0) and (year % 100 != 0):
    print(f"\n{year} is a leap year.")
else:
    print(f"\n{year} is NOT a leap year.")
