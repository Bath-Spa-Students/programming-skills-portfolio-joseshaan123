# Create a list called 'family' containing three names.
family = ['Shaan', 'Baiju', 'Grace']
# Create a message that combines "I'd like to invite " with the first name from the 'family' list (capitalized using the title() method) and "to dinner".
msg = "I'd like to invite " + family[0].title() + ", to dinner"
# Print the message, inviting the first person in the 'family' list to dinner.
print(msg)
# Repeat the process for the second person in the list, creating a message and printing it.
msg = "I'd like to invite " + family[1].title() + ", to dinner"
print(msg)
# Repeat the process for the third person in the list, creating a message and printing it.
msg = "I'd like to invite " + family[2].title() + ", to dinner"
print(msg)
# Create a message indicating that the second person in the list cannot come to dinner.
msg = "Sorry, " + family[1].title() + " cannot come for dinner"
# Print the message, informing that the second person can't attend dinner.
print(msg)
# Delete the second person from the 'family' list and replace them with 'eva'.
del family[1]
family.insert(1, 'eva')
# Create a message inviting the first person in the modified list to dinner and print it.
msg = "I'd like to invite " + family[0].title() + ", to dinner"
print(msg)
# Create a message inviting the second person (now 'eva') to dinner and print it.
msg = "I'd like to invite " + family[1].title() + ", to dinner"
print(msg)
# Create a message inviting the third person to dinner and print it.
msg = "I'd like to invite " + family[2].title() + ", to dinner"
print(msg)
