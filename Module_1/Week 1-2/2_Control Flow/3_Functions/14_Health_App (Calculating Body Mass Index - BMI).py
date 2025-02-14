def calculate_bmi(weight, height):
    """Calculates BMI (Body Mass Index)."""
    bmi = weight / (height ** 2)
    return round(bmi, 2)

# Real-world example:
weight = 70  # kg
height = 1.75  # meters
print("Your BMI is:", calculate_bmi(weight, height))  # Output: 22.86
