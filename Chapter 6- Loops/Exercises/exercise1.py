prompt = "\nWhat type of toppings would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"  Im adding {topping} to your pizza.")
    else:
        break