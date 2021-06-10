print("Follow prompts below to calculate your body mass index BMI")
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

num_height = float(height)
num_weight = float(weight)

BMI = round(num_weight / (num_height**2))
# BMI = str(BMI_as_int)
# BMI = weight / (height**2)

# using F-string automatically figures the datatype to be used
print(f"Your body mass index is {BMI}")