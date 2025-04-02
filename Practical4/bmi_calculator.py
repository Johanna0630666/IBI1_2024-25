# Pseudocode:
# 1. Let user input their weight (kg) and height (m)
# 2. Calculate BMI using formula: weight / (height^2)
# 3. Classify into categories:
#    If the BMI<18.5, the person is underweight
#    If the 18.5<=BMI<30, the person is normal weight
#    If the BMI>30, the person is obese
# 4. Output sentence with BMI value and category

# Actual code:
# Get user's input
weight = float(input("Enter your weight in kg: ")) #Get user's weight in kg
height = float(input("Enter your height in meters: ")) #Get user's height in meters

# Calculate BMI using the formula: weight / (height^2)
BMI = weight/(height *height)

# Determine the category based on BMI value
if BMI < 18.5:
    category = "underweight"
elif 18.5 <= BMI < 30:
    category = "normal weight"
else:
    category = "obese"

# Output sentence with BMI value and category
print("Your BMI is " + str(BMI) + ", and you are considered " + category + ".")
