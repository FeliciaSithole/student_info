name = input("What is your name? ")
surname = input("What is your surname? ")

full_name = f"{name} {surname}"

print(f"Welcome, {full_name}!")

print(f"Upper Case: {full_name.upper()}")
print(f"Title Case: {full_name.title()}")

birth_year = input("Enter your birth year: ")
age = 2026 - int(birth_year)

age_in_months = age * 12
print(f"Age: {age} years old ({age_in_months} months)")

fav_num = float(input("Enter your favourite number: "))
print(f"Favourite Number (rounded): {round(fav_num, 2)}")