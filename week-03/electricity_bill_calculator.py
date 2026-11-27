# Week 3 Task - Smart Electricity Bill Calculator
# slab logic + input validation

def read_units():
    # keep asking until the user enters a valid number
    while True:
        raw = input("Enter the units you used this month: ")
        if raw.replace('.', '', 1).isdigit():
            units = float(raw)
            if units >= 0:
                return units
            else:
                print("Units cannot be negative. Try again.")
        else:
            print("Please enter a valid number.")


def calculate_bill(units):
    # slab logic:
    # first 100 units -> Rs. 10 each
    # next 100 units (101-200) -> Rs. 15 each
    # above 200 units -> Rs. 20 each
    if units <= 100:
        bill = units * 10
    elif units <= 200:
        bill = 100 * 10 + (units - 100) * 15
    else:
        bill = 100 * 10 + 100 * 15 + (units - 200) * 20
    return bill


# main program
print("----- Smart Electricity Bill Calculator -----")
units = read_units()
bill = calculate_bill(units)
print("Units used :", units)
print("Total bill : Rs.", bill)
