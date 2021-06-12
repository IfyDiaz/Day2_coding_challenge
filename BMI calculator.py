print("Follow prompts below to calculate your body mass index BMI")
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

num_height = float(height)
num_weight = float(weight)

BMI = round(num_weight / (num_height**2))

# using F-string automatically figures the datatype to be used

if BMI < 18.5:
  print(f"Your BMI is {BMI} and it means you're underweight")
elif BMI < 25:
  print(f"Your BMI is {BMI} and it means you have a normal weight")
elif BMI < 30:
  print(f"Your BMI is {BMI} and it means you're slightly overweight")
elif BMI <= 35:
  print(f"Your BMI is {BMI} and it means you're obese")
else:
  print(f"Your BMI is {BMI} which is above 35. It means you're clinically obese")