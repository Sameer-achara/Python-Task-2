salary = float(input("Enter employee salary: "))
experience = int(input("Enter years of experience: "))

if experience >= 5:
    if salary >= 30000:
        bonus = salary * 0.10
        print("Bonus Amount:", bonus)
    else:
        print("Bonus not applicable due to salary criteria.")
else:
    print("Bonus not applicable due to experience criteria.")
