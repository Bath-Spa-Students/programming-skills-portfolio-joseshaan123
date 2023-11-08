# Set up a prompt asking the user for pizza toppings and how to exit the loop.
prompt = "\nWhat type of toppings would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

# Start an indefinite while loop, which will continue until 'break' is executed.
while True:
    # Prompt the user for a pizza topping.
    topping = input(prompt)
    
    # Check if the user input is not 'quit'; if not, print the chosen topping and continue the loop.
    if topping != 'quit':
        print(f"  I'm adding {topping} to your pizza.")
    # If the user inputs 'quit', break out of the loop to exit.
    else:
        break
