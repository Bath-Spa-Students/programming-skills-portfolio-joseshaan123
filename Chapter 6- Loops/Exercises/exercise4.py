# Create a list 'sandwich_orders' with various sandwich types and an empty list 'finished_sandwiches'.

sandwich_orders = ['Chicken', 'Zinger', 'Beef', 'Tuna']
finished_sandwiches = []
# Start a while loop that runs as long as there are items in 'sandwich_orders'.
# Inside the loop, remove the last sandwich from 'sandwich_orders' and store it in 'current_sandwich'.
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# After all sandwiches are prepared, print a newline for separation.
# Iterate through 'finished_sandwiches' and print a message for each sandwich that has been made.
print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")
