# Set the variable 'alien_color' to 'green'.
alien_color = 'green'

# Check if 'alien_color' is 'green' and print a message with 5 points if it is.
# If it's not 'green,' print a message with 10 points.
if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

# Update the 'alien_color' variable to 'yellow'.
alien_color = 'yellow'

# Check if 'alien_color' is 'green' (which it's not) and print a message with 10 points.
# Since it's not 'green,' the else block is executed.
if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")
