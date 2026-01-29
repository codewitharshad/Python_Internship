def make_bill(units):
    try:
        units = float(units)
    except ValueError:
        return "Invalid input, Units must be a number"
    
    if units <= 0:
        return "Units must be a positive number."
    
    if units <= 100:
        rate = units * 5
    elif units <= 300:
        rate = units * 7
    else:
        rate = units * 10

    return f"Total electricity bill for {units} units is ₹{rate}"


unit_count = input("Enter electricity units consumed: ")
print(make_bill(unit_count))