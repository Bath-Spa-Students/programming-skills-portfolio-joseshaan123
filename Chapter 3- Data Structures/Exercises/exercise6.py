# Create a list called 'family' containing three names.
family = ['Shaan', 'Baiju', 'Grace']

# Send dinner invitations to each person in the 'family' list.
msg = "I'd like to invite " + family[0].title() + ", to dinner"
print(msg)
msg = "I'd like to invite " + family[1].title() + ", to dinner"
print(msg)
msg = "I'd like to invite " + family[2].title() + ", to dinner"
print(msg)

# Print a message indicating that only two people can be invited to dinner.
print("\nSorry, we can only invite two people to dinner.")

# Send regret messages to the first two people in the 'family' list.
msg = "Sorry " + family[0].title() + ", you cannot be invited to dinner"
print(msg)
msg = "Sorry " + family[1].title() + ", you cannot be invited to dinner"
print(msg)

# Send dinner invitations to the last two people in the 'family' list.
msg = "I'd like to invite " + family[1].title() + ", to dinner"
print(msg)
msg = "I'd like to invite " + family[2].title() + ", to dinner"
print(msg)
#In this code, you are initially inviting three people to dinner, then informing them that only two can come.
# Finally, you send regrets to the first two and re-invite the last two to dinner.

