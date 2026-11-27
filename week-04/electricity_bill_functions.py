# Week 4 Task - Smart Electricity Bill Calculator (refactored into functions)
# same slab logic as week 3 but now everything is in small functions
# with docstrings, default arguments and clean PEP 8 names


def read_positive_number(prompt):
    """Keep asking the user until a valid positive number is entered."""
    while True:
        raw = input(prompt)
        if raw.replace('.', '', 1).isdigit():
            value = float(raw)
            if value >= 0:
                return value
        print("Invalid input. Please enter a positive number.")


def calculate_bill(units):
    """Return the bill using the slab rates:
    first 100 units Rs. 10, next 100 units Rs. 15, above that Rs. 20."""
    if units <= 100:
        return units * 10
    elif units <= 200:
        return 100 * 10 + (units - 100) * 15
    return 100 * 10 + 100 * 15 + (units - 200) * 20


def print_receipt(name, units, bill):
    """Print a small receipt for the customer."""
    print("-" * 30)
    print(f"Customer   : {name}")
    print(f"Units used : {units}")
    print(f"Total bill : Rs. {bill}")
    print("-" * 30)


def main():
    """Run the calculator once."""
    print("----- Smart Electricity Bill Calculator -----")
    name = input("Customer name: ")
    units = read_positive_number("Units used this month: ")
    bill = calculate_bill(units)
    print_receipt(name, units, bill)


# sample runs
# run 1: name = Ali, units = 80  -> bill = Rs. 800.0
# run 2: name = Sara, units = 150 -> bill = Rs. 1750.0
# run 3: name = Hamza, units = 260 -> bill = Rs. 4200.0

if __name__ == "__main__":
    main()
