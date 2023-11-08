# Set up a prompt asking the user for their age and how to exit the loop.
ticket = "\nHow old are you?"
ticket += "\nEnter 'quit' when you are finished. "

# Start an indefinite while loop, which will continue until 'break' is executed.
while True:
    # Prompt the user for their age.
    age = input(ticket)
    
    # Check if the user input is 'quit'; if so, break out of the loop to exit.
    if age == 'quit':
        break

    # Convert the user's age input to an integer for comparison.
    age = int(age)

    # Check the age and print the appropriate ticket price.
    if age < 3:
        print("  You are free of cost!")
    elif age < 13:
        print("  Your ticket costs $10.")
    else:
        print("  Your ticket costs $15.")
