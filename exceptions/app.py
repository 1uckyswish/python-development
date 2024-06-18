try:
    age = int(input("Age: "))
except ValueError:
    print("Sorry try again")
else:
    print("no exception was thrown")