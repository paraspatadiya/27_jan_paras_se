age = int(input("Enter age: "))
weight = int(input("Enter weight: "))
if age >= 18:
    if weight >= 55:
        print("Eligible to donate blood")
    else:
        print("Not eligible")
else:
    print("Not eligible")