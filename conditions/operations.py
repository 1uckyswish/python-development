high_income = True
good_credit = True
student = True

if high_income and good_credit:
    print("NEW car")
elif high_income and not good_credit:
    print("Check back later")
else:
    print("Sorry")


age = 22

if 18 <= age < 65:
    print("Welcome")
