ticket= "\nHow old are you?"
ticket += "\nEnter 'quit' when you are finished. "

while True:
    age = input(ticket)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You are free of cost!")
    elif age < 13:
        print("  Your ticket costs $10.")
    else:
        print("  Your ticket costs $15.")