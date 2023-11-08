# Prompt the user to enter the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Compute the area of the circle
pi = 3.14159  # You can also use the math.pi constant
area = pi * (radius ** 2)

# Display the result
print(f"The area of the circle with radius {radius} is {area:.2f}")
