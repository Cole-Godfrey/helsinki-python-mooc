# Write your solution here
value = int(input("Value of gift: "))
tax = 0
base_tax = 0
lower_limit = 0
tax_rate = 0
if 5000 <= value < 25000:
    base_tax = 100
    lower_limit = 5000
    tax_rate = 0.08
elif 25000 <= value < 55000:
    base_tax = 1700
    lower_limit = 25000
    tax_rate = 0.10
elif 55000 <= value < 200000:
    base_tax = 4700
    lower_limit = 55000
    tax_rate = 0.12
elif 200000 <= value < 1000000:
    base_tax = 22100
    lower_limit = 200000
    tax_rate = 0.15
elif value >= 1000000:
    base_tax = 142100
    lower_limit = 1000000
    tax_rate = 0.17

tax = base_tax + (value - lower_limit) * tax_rate
if tax == 0:
    print("No tax!")
else:
    print(f"Amount of tax: {tax} euros")
