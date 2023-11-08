# Set the variable 'age' to 18.
age = 18

# Check if 'age' is less than 2 and print a message for babies if it is.
# If not, check if 'age' is less than 4 and print a message for toddlers.
# Continue checking for different age ranges and print appropriate messages.
# The 'else' block will catch any age not covered by the previous conditions.
if age < 2:
    print("You are a baby!")
elif age < 4:
    print("You are a toddler!")
elif age < 13:
    print("You are a kid!")
elif age < 20:
    print("You are a teenager!")
elif age < 65:
    print("You are an adult!")
else:
    print("You are an elder!")
