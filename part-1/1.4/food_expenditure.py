# Write your solution here
times_a_week = int(input("How many times a week do you eat at the student cafeteria? "))
student_lunch_price = float(input("The price of a typical student lunch? "))
weekly_groceries_price = float(input("How much money do you spend on groceries in a week? "))
weekly = times_a_week * student_lunch_price + weekly_groceries_price
daily = weekly / 7
print("Average food expenditure:")
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")