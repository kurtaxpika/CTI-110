# LaRicia Leach
# 10/08/2024
# P2LAB1
# Using Python's built-in math library

# Import math history
import math

print(f"The value of pi is {math.pi}\n")

# Get radius from user
radius = float(input("What is the radius of the circle?"))
print()

# Calculate the diameter
diameter = 2 * radius

# Display diameter with one decimal place
print(f"The dianeter of the circle is {diameter:.1f}\n")

# Calculate the circumference
circumf = 2 * math.pi * radius

# Display the circumference
print(f"The circumfrence of the circle is {circumf:.2f}\n")

# Calculate the area

area = math.pi * math.pow(radius, 2)

# Display the area

print(f"The area of the circle is {area:.3f}")
