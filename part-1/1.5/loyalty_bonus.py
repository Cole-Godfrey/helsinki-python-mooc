# Fix the program
points = int(input("How many points are on your card? "))
bonus_points = 0
if points < 100:
    bonus_points = points * 0.1
    print("Your bonus is 10 %")

if points >= 100:
    bonus_points = points * 0.15
    print("Your bonus is 15 %")

points += bonus_points
print("You now have", points, "points")