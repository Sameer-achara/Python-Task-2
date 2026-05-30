balance = 799

amount = float(input("Enter withdrawal amount: "))

if amount > 0:
    if amount <= balance:
        balance = balance-amount
        print("Withdrawal successful.")
        print("Remaining Balance:", balance)
    else:
        print("Insufficient balance.")
else:
    print("Invalid withdrawal amount.")
