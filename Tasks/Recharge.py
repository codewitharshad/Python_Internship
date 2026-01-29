def recharge(phoneNo, amount):

    if len(phoneNo) != 10:
        return "Invalid Number! Number must be exactly 10-digits."
    if not phoneNo.isdigit():
            return "Mobile number should contain only digits."

    try:
        amount = int(amount)
    except ValueError:
         return "Recharge amount must be a number."
    
    if amount < 10: 
        return "Minimum recharge amount must be greater than ₹10."
    
    return f"Recharge of {amount} is successfully done on {phoneNo}"
    

phoneNo = str(input("Enter your 10-digit mobile number : "))
amount = input("Enter the recharge amount : ")

print(recharge(phoneNo, amount))