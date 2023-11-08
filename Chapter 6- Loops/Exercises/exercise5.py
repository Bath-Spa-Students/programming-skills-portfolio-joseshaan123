# Create a list 'sandwich_orders' with various sandwich types, including 'pastrami',
# and an empty list 'finished_sandwiches'.
sandwich_orders = [
    'pastrami', 'Chicken', 'tuna', 'pastrami',
    'Beef', 'Zinger', 'pastrami']
finished_sandwiches = []

# Inform customers that pastrami is unavailable and remove all instances of 'pastrami' from 'sandwich_orders'.
print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
# Print a newline for separation.
# Start a while loop that runs as long as there are items in 'sandwich_orders'.
# Inside the loop, remove the last sandwich from 'sandwich_orders' and store it in 'current_sandwich'.
# Print a message indicating the preparation of the current sandwich and add it to 'finished_sandwiches'.
print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# After all sandwiches are prepared, print a newline for separation.
# Iterate through 'finished_sandwiches' and print a message for each sandwich that has been made.
print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")
