# Write your solution here
year = int(input("Year: "))
original_year = year
while True:
    year += 1
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                break
        else:
            break

print(f"The next leap year after {original_year} is {year}")