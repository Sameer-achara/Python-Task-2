marks = float(input("Enter your marks percentage: "))
age = int(input("Enter your age: "))

if marks >= 60:
    if age >= 18:
        print("Eligible for college admission.")
    else:
        print("Not Eligible: Age requirement not met.")
else:
    print("Not Eligible: Insufficient marks.")
