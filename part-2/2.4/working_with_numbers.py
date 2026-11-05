# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")

numbers = 0
s = 0
pos_nums = 0
neg_nums = 0

while True:
    num = int(input("Number: "))
    if num == 0:
        break
    numbers += 1
    s += num
    if num > 0:
        pos_nums += 1
    else:
        neg_nums += 1

mean = s / numbers

print(f"Numbers typed in {numbers}")
print(f"The sum of the numbers is {s}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {pos_nums}")
print(f"Negative numbers {neg_nums}")
