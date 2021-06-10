print("If you were to live up to 90 years, this code will tell you how long you have left")
age = input("What is your current age? ")

target_age = 90 - int(age)
target_in_days = target_age * 365 
target_in_weeks = target_age * 54
target_in_months = target_age * 12

print(f"You have {target_in_days} days, {target_in_weeks} weeks and {target_in_months} Months left.")
