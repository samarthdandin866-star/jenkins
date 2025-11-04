# Simple Interest Calculation

# Taking inputs from the user
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest (in %): "))
time = float(input("Enter Time (in years): "))

# Calculating Simple Interest
simple_interest = (principal * rate * time) / 100

# Displaying the result
print("Simple Interest =", simple_interest)
