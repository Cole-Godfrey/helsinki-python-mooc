# Write your solution here
password = input("Password: ")

while True:
    repeated_password = input("Repeat password: ")
    if password == repeated_password:
        print("User account created!")
        break
    else:
        print("They do not match!")