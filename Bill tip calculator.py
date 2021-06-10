print("Welcome to the tip calculator. ")

total_bill = input("What's the total bill? $")
total_bill_float = float(total_bill)

percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")
percentage_in_integer = int(percentage)
percentage_tip_add = (percentage_in_integer/100) * total_bill_float

divider = input("how many people to split the bill? ")
divider_in_int = int(divider)

percentage_tip_total = total_bill_float + percentage_tip_add
percentage_tip = round(percentage_tip_total/divider_in_int,2)
percentage_tip = "{:.2f}".format(percentage_tip)

print(f"Each person should pay: ${percentage_tip}")